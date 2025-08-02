"""
画像アップロード機能のDjangoビュー
クリップボードからの画像保存をサポート
"""

import os
import uuid
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def upload_project_image(request):
    """
    プロジェクト画像アップロード
    
    POST /api/v1/projects/images/upload/
    Content-Type: multipart/form-data
    
    Parameters:
    - image: 画像ファイル（blob）
    - project_id: プロジェクトID
    - timestamp: タイムスタンプ（オプション）
    """
    try:
        # パラメータ取得
        image_file = request.FILES.get('image')
        project_id = request.POST.get('project_id')
        timestamp = request.POST.get('timestamp')
        
        if not image_file:
            return JsonResponse({
                'error': 'No image file provided'
            }, status=400)
            
        if not project_id:
            return JsonResponse({
                'error': 'project_id is required'
            }, status=400)
        
        # プロジェクトディレクトリの確認・作成
        project_base_path = getattr(settings, 'PROJECTS_ROOT', '/home/futaro/project/StatVizForge_JikkenPy/project')
        project_path = os.path.join(project_base_path, project_id)
        
        if not os.path.exists(project_path):
            logger.warning(f"Project directory not found: {project_path}")
            return JsonResponse({
                'error': f'Project directory not found: {project_id}'
            }, status=404)
        
        # 画像保存ディレクトリの作成
        screenshots_path = os.path.join(project_path, 'screenshots')
        os.makedirs(screenshots_path, exist_ok=True)
        
        # ファイル名生成
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                timestamp_str = dt.strftime('%Y%m%d_%H%M%S')
            except ValueError:
                timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
        else:
            timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # ファイル拡張子の決定
        content_type = image_file.content_type or 'image/png'
        extension_map = {
            'image/png': 'png',
            'image/jpeg': 'jpg',
            'image/jpg': 'jpg',
            'image/gif': 'gif',
            'image/webp': 'webp',
            'image/bmp': 'bmp'
        }
        extension = extension_map.get(content_type, 'png')
        
        # 一意のファイル名生成（衝突回避）
        unique_id = str(uuid.uuid4())[:8]
        filename = f"screenshot_{timestamp_str}_{unique_id}.{extension}"
        file_path = os.path.join(screenshots_path, filename)
        
        # ファイル保存
        with open(file_path, 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)
        
        # レスポンス準備
        file_size = os.path.getsize(file_path)
        relative_path = os.path.relpath(file_path, project_base_path)
        
        response_data = {
            'success': True,
            'filename': filename,
            'filepath': relative_path,
            'size': file_size,
            'content_type': content_type,
            'timestamp': datetime.now().isoformat(),
            'project_id': project_id,
            'url': f'/api/v1/projects/{project_id}/files/{relative_path}'
        }
        
        logger.info(f"Image uploaded successfully: {filename} ({file_size} bytes) to project {project_id}")
        
        return JsonResponse(response_data)
        
    except Exception as e:
        logger.error(f"Image upload error: {str(e)}", exc_info=True)
        return JsonResponse({
            'error': 'Internal server error',
            'details': str(e)
        }, status=500)


@require_http_methods(["GET"])
def list_project_images(request, project_id):
    """
    プロジェクトの画像一覧取得
    
    GET /api/v1/projects/{project_id}/images/
    """
    try:
        project_base_path = getattr(settings, 'PROJECTS_ROOT', '/home/futaro/project/StatVizForge_JikkenPy/project')
        screenshots_path = os.path.join(project_base_path, project_id, 'screenshots')
        
        if not os.path.exists(screenshots_path):
            return JsonResponse({
                'images': [],
                'project_id': project_id,
                'message': 'No screenshots directory found'
            })
        
        images = []
        for filename in os.listdir(screenshots_path):
            file_path = os.path.join(screenshots_path, filename)
            if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp')):
                stat = os.stat(file_path)
                relative_path = os.path.relpath(file_path, project_base_path)
                
                images.append({
                    'filename': filename,
                    'filepath': relative_path,
                    'size': stat.st_size,
                    'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'url': f'/api/v1/projects/{project_id}/files/{relative_path}'
                })
        
        # 作成日時でソート（新しいものから）
        images.sort(key=lambda x: x['created'], reverse=True)
        
        return JsonResponse({
            'images': images,
            'project_id': project_id,
            'count': len(images)
        })
        
    except Exception as e:
        logger.error(f"List images error: {str(e)}", exc_info=True)
        return JsonResponse({
            'error': 'Internal server error',
            'details': str(e)
        }, status=500)


@require_http_methods(["DELETE"])
def delete_project_image(request, project_id, filename):
    """
    プロジェクト画像削除
    
    DELETE /api/v1/projects/{project_id}/images/{filename}
    """
    try:
        project_base_path = getattr(settings, 'PROJECTS_ROOT', '/home/futaro/project/StatVizForge_JikkenPy/project')
        file_path = os.path.join(project_base_path, project_id, 'screenshots', filename)
        
        if not os.path.exists(file_path):
            return JsonResponse({
                'error': 'Image file not found'
            }, status=404)
        
        # セキュリティチェック: パストラバーサル攻撃防止
        screenshots_path = os.path.join(project_base_path, project_id, 'screenshots')
        if not os.path.commonpath([screenshots_path, file_path]) == screenshots_path:
            return JsonResponse({
                'error': 'Invalid file path'
            }, status=400)
        
        os.remove(file_path)
        
        logger.info(f"Image deleted: {filename} from project {project_id}")
        
        return JsonResponse({
            'success': True,
            'message': f'Image {filename} deleted successfully',
            'project_id': project_id,
            'filename': filename
        })
        
    except Exception as e:
        logger.error(f"Delete image error: {str(e)}", exc_info=True)
        return JsonResponse({
            'error': 'Internal server error',
            'details': str(e)
        }, status=500)