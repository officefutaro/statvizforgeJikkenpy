#!/usr/bin/env python3
"""
フロントエンド・バックエンドAPI整合性テスト
このスクリプトは両側のAPIエンドポイントと型定義の整合性を確認します。
"""
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

# プロジェクトルートを取得
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# バックエンドのパス追加
BACKEND_PATH = PROJECT_ROOT / "app" / "backend"
sys.path.insert(0, str(BACKEND_PATH))

# Django設定の初期化
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from api.urls import urlpatterns

class APIIntegrationTester:
    def __init__(self):
        self.backend_endpoints = set()
        self.frontend_endpoints = set()
        self.mismatches = []
        self.missing_in_frontend = []
        self.missing_in_backend = []
        self.results = {
            'test_date': datetime.now().isoformat(),
            'endpoint_coverage': {},
            'type_mismatches': [],
            'missing_implementations': [],
            'recommendations': []
        }
    
    def extract_backend_endpoints(self):
        """バックエンドのエンドポイントを抽出 - APIドキュメントから"""
        # doc/APIja.mdから正確なエンドポイント一覧を取得
        api_doc_path = PROJECT_ROOT / "doc" / "APIja.md"
        endpoints = []
        
        if api_doc_path.exists():
            with open(api_doc_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # APIエンドポイントパターンを抽出
                # GET /api/v1/projects/ のような形式
                endpoint_patterns = re.findall(r'```\n(GET|POST|PUT|DELETE|PATCH)\s+(/api/v1/[^\n]+)\n```', content)
                
                for method, path in endpoint_patterns:
                    # パラメータを正規化
                    normalized_path = path
                    normalized_path = re.sub(r'{[^}]+}', '{}', normalized_path)  # {id} -> {}
                    
                    endpoints.append({
                        'path': normalized_path,
                        'method': method,
                        'documented': True
                    })
        
        # 実際のurls.pyからも抽出して補完
        try:
            from config.urls import urlpatterns as root_urlpatterns
            
            def extract_from_patterns(patterns, prefix=''):
                for pattern in patterns:
                    if hasattr(pattern, 'url_patterns'):
                        new_prefix = prefix + str(pattern.pattern)
                        extract_from_patterns(pattern.url_patterns, new_prefix)
                    else:
                        path_str = str(pattern.pattern)
                        if path_str.startswith('^'):
                            path_str = path_str[1:]
                        if path_str.endswith('$'):
                            path_str = path_str[:-1]
                        
                        full_path = prefix + path_str
                        if 'api/v1' in full_path:
                            # 正規化
                            normalized = '/' + full_path
                            normalized = re.sub(r'<[^>]+>', '{}', normalized)
                            normalized = re.sub(r'\(\?P<[^>]+>[^)]+\)', '{}', normalized)
                            normalized = normalized.replace('//', '/')
                            
                            # 既存エンドポイントに含まれていない場合のみ追加
                            if not any(ep['path'] == normalized for ep in endpoints):
                                endpoints.append({
                                    'path': normalized,
                                    'method': 'GET',  # デフォルト
                                    'documented': False
                                })
            
            extract_from_patterns(root_urlpatterns)
        except Exception as e:
            print(f"   警告: urls.pyからの抽出でエラー: {e}")
        
        self.backend_endpoints = endpoints
        return endpoints
    
    def extract_frontend_endpoints(self):
        """フロントエンドのエンドポイントを抽出"""
        api_client_path = PROJECT_ROOT / "app" / "frontend" / "src" / "services" / "api-client.ts"
        api_service_path = PROJECT_ROOT / "app" / "frontend" / "src" / "services" / "api.ts"
        
        endpoints = []
        
        # api-client.ts から抽出
        if api_client_path.exists():
            with open(api_client_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # API URLパターンを抽出
                url_patterns = re.findall(r'`\${API_BASE_URL}([^`]+)`', content)
                for pattern in url_patterns:
                    # メソッドを推測
                    method = 'GET'
                    if 'create' in pattern or 'POST' in content[:content.find(pattern)]:
                        method = 'POST'
                    elif 'update' in pattern or 'PUT' in content[:content.find(pattern)]:
                        method = 'PUT'
                    elif 'delete' in pattern or 'DELETE' in content[:content.find(pattern)]:
                        method = 'DELETE'
                    
                    endpoints.append({
                        'path': f'/api/v1{pattern}',
                        'method': method,
                        'file': 'api-client.ts'
                    })
        
        # api.ts から抽出
        if api_service_path.exists():
            with open(api_service_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # fetch呼び出しパターンを抽出
                fetch_patterns = re.findall(r'fetch\([\'"`]([^\'"`]+)[\'"`]', content)
                for pattern in fetch_patterns:
                    if '/api/' in pattern:
                        endpoints.append({
                            'path': pattern,
                            'method': 'GET',  # デフォルト
                            'file': 'api.ts'
                        })
        
        self.frontend_endpoints = endpoints
        return endpoints
    
    def compare_endpoints(self):
        """エンドポイントの比較と整合性チェック"""
        # バックエンドのパスを正規化
        backend_paths = {}
        for endpoint in self.backend_endpoints:
            path = endpoint['path']
            # パラメータを統一形式に
            path = re.sub(r'{[^}]+}', '{}', path)
            path = re.sub(r'<[^>]+>', '{}', path)
            path = re.sub(r'\(\?P<[^>]+>[^)]+\)', '{}', path)
            # 末尾スラッシュを統一（あり）
            if not path.endswith('/'):
                path += '/'
            backend_paths[path] = endpoint
        
        # フロントエンドのパスを正規化
        frontend_paths = {}
        for endpoint in self.frontend_endpoints:
            path = endpoint['path']
            # 変数を統一形式に
            path = re.sub(r'\${[^}]+}', '{}', path)
            path = re.sub(r'/\$\{[^}]+\}', '/{}', path)
            # 末尾スラッシュを統一（あり）
            if not path.endswith('/'):
                path += '/'
            frontend_paths[path] = endpoint
        
        # 比較
        backend_set = set(backend_paths.keys())
        frontend_set = set(frontend_paths.keys())
        
        self.missing_in_frontend = list(backend_set - frontend_set)
        self.missing_in_backend = list(frontend_set - backend_set)
        
        # 実装済みのエンドポイント
        implemented = backend_set & frontend_set
        
        # カバレッジ計算
        # APIja.mdに記載されているエンドポイントのうち、実装されているものの割合
        documented_endpoints = [ep for ep in self.backend_endpoints if ep.get('documented', False)]
        if documented_endpoints:
            documented_paths = set()
            for ep in documented_endpoints:
                path = ep['path']
                path = re.sub(r'{[^}]+}', '{}', path)
                if not path.endswith('/'):
                    path += '/'
                documented_paths.add(path)
            
            implemented_documented = documented_paths & frontend_set
            coverage = (len(implemented_documented) / len(documented_paths) * 100) if documented_paths else 0
        else:
            # ドキュメントがない場合は全体のカバレッジ
            total = len(backend_set | frontend_set)
            coverage = (len(implemented) / total * 100) if total > 0 else 0
        
        self.results['endpoint_coverage'] = {
            'total_endpoints': len(backend_set),
            'frontend_endpoints': len(frontend_set),
            'implemented_endpoints': len(implemented),
            'coverage_percentage': coverage,
            'missing_in_frontend': sorted(self.missing_in_frontend),
            'missing_in_backend': sorted(self.missing_in_backend)
        }
    
    def check_type_consistency(self):
        """型定義の整合性チェック"""
        # TypeScriptインターフェースの抽出
        interface_path = PROJECT_ROOT / "app" / "frontend" / "src" / "services" / "api-client.ts"
        if interface_path.exists():
            with open(interface_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Project interfaceの確認
                project_interface = re.search(r'export interface Project \{([^}]+)\}', content, re.DOTALL)
                if project_interface:
                    ts_fields = set(re.findall(r'(\w+)[?]?:', project_interface.group(1)))
                    
                    # Djangoシリアライザーとの比較
                    from api.serializers import ProjectSerializer
                    django_fields = set(ProjectSerializer.Meta.fields) if hasattr(ProjectSerializer.Meta, 'fields') else set()
                    
                    missing_in_ts = django_fields - ts_fields
                    missing_in_django = ts_fields - django_fields
                    
                    if missing_in_ts or missing_in_django:
                        self.results['type_mismatches'].append({
                            'interface': 'Project',
                            'missing_in_typescript': list(missing_in_ts),
                            'missing_in_django': list(missing_in_django)
                        })
    
    def generate_recommendations(self):
        """改善提案の生成"""
        recommendations = []
        
        # カバレッジが低い場合
        if self.results['endpoint_coverage']['coverage_percentage'] < 80:
            recommendations.append("エンドポイントカバレッジが80%未満です。未実装のエンドポイントを確認してください。")
        
        # 型不整合がある場合
        if self.results['type_mismatches']:
            recommendations.append("TypeScriptインターフェースとDjangoシリアライザーの型定義に不整合があります。")
        
        # フロントエンドに未実装のエンドポイント
        if self.missing_in_frontend:
            recommendations.append(f"フロントエンドに{len(self.missing_in_frontend)}個の未実装エンドポイントがあります。")
        
        # バックエンドに未実装のエンドポイント
        if self.missing_in_backend:
            recommendations.append(f"バックエンドに{len(self.missing_in_backend)}個の未実装エンドポイントがあります。")
        
        self.results['recommendations'] = recommendations
    
    def save_report(self):
        """レポートをMarkdownファイルに保存"""
        report_dir = PROJECT_ROOT / "doc" / "history"
        report_dir.mkdir(parents=True, exist_ok=True)
        
        date_str = datetime.now().strftime("%Y%m%d")
        report_path = report_dir / f"api_integration_{date_str}.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# API整合性テストレポート - {datetime.now().strftime('%Y年%m月%d日')}\n\n")
            
            # サマリー
            f.write("## サマリー\n\n")
            coverage = self.results['endpoint_coverage']
            f.write(f"- **総エンドポイント数**: {coverage['total_endpoints']}\n")
            f.write(f"- **実装済みエンドポイント数**: {coverage['implemented_endpoints']}\n")
            f.write(f"- **カバレッジ**: {coverage['coverage_percentage']:.1f}%\n\n")
            
            # 未実装エンドポイント
            if coverage['missing_in_frontend']:
                f.write("## フロントエンド未実装エンドポイント\n\n")
                for endpoint in sorted(coverage['missing_in_frontend']):
                    f.write(f"- [ ] {endpoint}\n")
                f.write("\n")
            
            if coverage['missing_in_backend']:
                f.write("## バックエンド未実装エンドポイント\n\n")
                for endpoint in sorted(coverage['missing_in_backend']):
                    f.write(f"- [ ] {endpoint}\n")
                f.write("\n")
            
            # 型不整合
            if self.results['type_mismatches']:
                f.write("## 型定義の不整合\n\n")
                for mismatch in self.results['type_mismatches']:
                    f.write(f"### {mismatch['interface']}\n\n")
                    if mismatch['missing_in_typescript']:
                        f.write("**TypeScriptに不足**:\n")
                        for field in mismatch['missing_in_typescript']:
                            f.write(f"- {field}\n")
                    if mismatch['missing_in_django']:
                        f.write("**Djangoに不足**:\n")
                        for field in mismatch['missing_in_django']:
                            f.write(f"- {field}\n")
                    f.write("\n")
            
            # 改善提案
            if self.results['recommendations']:
                f.write("## 改善提案\n\n")
                for rec in self.results['recommendations']:
                    f.write(f"- {rec}\n")
        
        print(f"レポートを保存しました: {report_path}")
        return report_path
    
    def run_tests(self):
        """全テストを実行"""
        print("=== API整合性テスト開始 ===\n")
        
        print("1. バックエンドエンドポイント抽出中...")
        self.extract_backend_endpoints()
        print(f"   {len(self.backend_endpoints)}個のエンドポイントを検出")
        
        print("\n2. フロントエンドエンドポイント抽出中...")
        self.extract_frontend_endpoints()
        print(f"   {len(self.frontend_endpoints)}個のエンドポイントを検出")
        
        print("\n3. エンドポイント比較中...")
        self.compare_endpoints()
        
        print("\n4. 型整合性チェック中...")
        self.check_type_consistency()
        
        print("\n5. 改善提案生成中...")
        self.generate_recommendations()
        
        print("\n6. レポート保存中...")
        report_path = self.save_report()
        
        print("\n=== テスト完了 ===")
        print(f"\nカバレッジ: {self.results['endpoint_coverage']['coverage_percentage']:.1f}%")
        
        # テスト失敗判定
        if self.results['endpoint_coverage']['coverage_percentage'] < 70:
            print("\n❌ テスト失敗: カバレッジが70%未満です")
            return False
        
        print("\n✅ テスト成功")
        return True


if __name__ == "__main__":
    tester = APIIntegrationTester()
    success = tester.run_tests()
    sys.exit(0 if success else 1)