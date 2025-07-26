# 言語ローカライゼーション用ユーティリティ

# エラーメッセージの多言語辞書
ERROR_MESSAGES = {
    'VALIDATION_ERROR': {
        'en': 'Invalid input data',
        'ja': '入力データが不正です',
        'zh': '输入数据无效'
    },
    'DUPLICATE_FOLDER': {
        'en': 'A project with this folder name already exists',
        'ja': '同じフォルダ名のプロジェクトが既に存在します',
        'zh': '具有此文件夹名称的项目已存在'
    },
    'INTERNAL_ERROR': {
        'en': 'An unexpected error occurred. Please try again later',
        'ja': '予期しないエラーが発生しました。しばらく経ってから再試行してください',
        'zh': '发生意外错误。请稍后重试'
    },
    'PROJECT_NOT_FOUND': {
        'en': 'Project not found',
        'ja': 'プロジェクトが見つかりません',
        'zh': '未找到项目'
    },
    'FAILED_TO_CREATE_PROJECT': {
        'en': 'Failed to create project',
        'ja': 'プロジェクトの作成に失敗しました',
        'zh': '项目创建失败'
    },
    'FAILED_TO_LOAD_PROJECTS': {
        'en': 'Failed to load projects registry',
        'ja': 'プロジェクト一覧の読み込みに失敗しました',
        'zh': '加载项目注册表失败'
    },
    'FAILED_TO_UPDATE_PROJECT': {
        'en': 'Failed to update project',
        'ja': 'プロジェクトの更新に失敗しました',
        'zh': '项目更新失败'
    },
    'FAILED_TO_DELETE_PROJECT': {
        'en': 'Failed to delete project',
        'ja': 'プロジェクトの削除に失敗しました',
        'zh': '项目删除失败'
    },
    'FAILED_TO_ARCHIVE_PROJECT': {
        'en': 'Failed to archive project',
        'ja': 'プロジェクトのアーカイブに失敗しました',
        'zh': '项目归档失败'
    },
    'FAILED_TO_LOAD_DELETED_PROJECTS': {
        'en': 'Failed to load deleted projects',
        'ja': '削除済みプロジェクトの読み込みに失敗しました',
        'zh': '加载已删除项目失败'
    },
    'NO_DELETED_PROJECTS': {
        'en': 'No deleted projects found',
        'ja': '削除済みプロジェクトが見つかりません',
        'zh': '未找到已删除的项目'
    },
    'DELETED_PROJECT_NOT_FOUND': {
        'en': 'Deleted project not found',
        'ja': '削除済みプロジェクトが見つかりません',
        'zh': '未找到已删除的项目'
    },
    'ARCHIVE_FILE_NOT_FOUND': {
        'en': 'Archive file not found',
        'ja': 'アーカイブファイルが見つかりません',
        'zh': '未找到归档文件'
    },
    'PROJECT_FOLDER_ALREADY_EXISTS': {
        'en': 'Project folder already exists',
        'ja': 'プロジェクトフォルダが既に存在します',
        'zh': '项目文件夹已存在'
    },
    'FAILED_TO_EXTRACT_ARCHIVE': {
        'en': 'Failed to extract archive',
        'ja': 'アーカイブの展開に失敗しました',
        'zh': '解压归档失败'
    },
    'FAILED_TO_RESTORE_PROJECT': {
        'en': 'Failed to restore project',
        'ja': 'プロジェクトの復元に失敗しました',
        'zh': '恢复项目失败'
    }
}

# フィールドバリデーションメッセージ
FIELD_VALIDATION_MESSAGES = {
    'folder_name': {
        'required': {
            'en': 'This field is required',
            'ja': 'この項目は必須です',
            'zh': '此字段为必填项'
        },
        'already_exists': {
            'en': 'Folder name already exists',
            'ja': 'フォルダ名が既に存在します',
            'zh': '文件夹名称已存在'
        }
    },
    'project_name': {
        'required': {
            'en': 'This field is required',
            'ja': 'この項目は必須です',
            'zh': '此字段为必填项'
        },
        'max_length': {
            'en': 'Project name must be 255 characters or less',
            'ja': 'プロジェクト名は255文字以内で入力してください',
            'zh': '项目名称不得超过255个字符'
        }
    },
    'description': {
        'required': {
            'en': 'This field is required',
            'ja': 'この項目は必須です',
            'zh': '此字段为必填项'
        }
    }
}

SUPPORTED_LANGUAGES = ['en', 'ja', 'zh']
DEFAULT_LANGUAGE = 'en'


def get_language_from_request(request):
    """リクエストから言語コードを取得"""
    lang = request.GET.get('lang', DEFAULT_LANGUAGE)
    return lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE


def get_error_message(error_code, language='en'):
    """エラーコードと言語から適切なエラーメッセージを取得"""
    if error_code not in ERROR_MESSAGES:
        return ERROR_MESSAGES['INTERNAL_ERROR'][language]
    
    if language not in ERROR_MESSAGES[error_code]:
        language = DEFAULT_LANGUAGE
    
    return ERROR_MESSAGES[error_code][language]


def get_field_validation_message(field_name, validation_type, language='en'):
    """フィールドバリデーションメッセージを取得"""
    if field_name not in FIELD_VALIDATION_MESSAGES:
        return get_error_message('VALIDATION_ERROR', language)
    
    if validation_type not in FIELD_VALIDATION_MESSAGES[field_name]:
        return get_error_message('VALIDATION_ERROR', language)
    
    if language not in FIELD_VALIDATION_MESSAGES[field_name][validation_type]:
        language = DEFAULT_LANGUAGE
    
    return FIELD_VALIDATION_MESSAGES[field_name][validation_type][language]


def create_error_response(error_code, language='en', details=None, status_code=400):
    """標準化されたエラーレスポンスを作成"""
    from rest_framework.response import Response
    
    response_data = {
        'error': error_code,
        'message': get_error_message(error_code, language)
    }
    
    if details:
        response_data['details'] = details
    
    return Response(response_data, status=status_code)