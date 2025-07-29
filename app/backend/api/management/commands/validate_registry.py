"""
プロジェクトレジストリの整合性を手動で確認・修正するDjangoコマンド
"""
from django.core.management.base import BaseCommand
from api.registry_validator import validate_and_fix_registry


class Command(BaseCommand):
    help = 'プロジェクトレジストリとフォルダ構造の整合性を確認・修正します'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='修正を実行せずに問題点のみレポート',
        )
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('プロジェクトレジストリの整合性確認を開始...'))
        
        if options['dry_run']:
            self.stdout.write(self.style.WARNING('DRY RUN モード: 修正は実行されません'))
        
        try:
            modified, log_messages = validate_and_fix_registry()
            
            if log_messages:
                self.stdout.write('\n=== 整合性確認結果 ===')
                for message in log_messages:
                    if '削除' in message or 'エラー' in message:
                        self.stdout.write(self.style.WARNING(f'⚠ {message}'))
                    elif '作成' in message or '復元' in message:
                        self.stdout.write(self.style.SUCCESS(f'✓ {message}'))
                    else:
                        self.stdout.write(f'• {message}')
                
                if modified:
                    self.stdout.write(
                        self.style.SUCCESS('\n✓ 整合性確認完了: 修正が適用されました')
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS('\n✓ 整合性確認完了: 修正は不要でした')
                    )
            else:
                self.stdout.write(
                    self.style.SUCCESS('✓ レジストリは正常です。修正は不要でした。')
                )
        
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'✗ 整合性確認中にエラーが発生しました: {e}')
            )
            raise