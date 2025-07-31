"""
WSL2対応のカスタムrunserverコマンド
常に0.0.0.0:8000でバインドしてWindows Chromeからアクセス可能にする
"""

from django.core.management.commands.runserver import Command as RunserverCommand
from django.conf import settings
import sys


class Command(RunserverCommand):
    help = 'WSL2対応の開発サーバー起動（自動的に0.0.0.0:8000でバインド）'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--force-localhost',
            action='store_true',
            help='強制的に127.0.0.1でバインド（WSL2対応を無効化）',
        )

    def handle(self, *args, **options):
        # デフォルトアドレスを0.0.0.0:8000に設定
        if not options['addrport']:
            if options.get('force_localhost'):
                options['addrport'] = '127.0.0.1:8000'
                self.stdout.write(
                    self.style.WARNING('🔒 localhost(127.0.0.1)モードで起動 - Windows Chromeからアクセス不可')
                )
            else:
                options['addrport'] = '0.0.0.0:8000'
                self.stdout.write(
                    self.style.SUCCESS('🌐 WSL2対応モードで起動 - Windows Chromeからアクセス可能')
                )
        
        # アドレスポートの解析
        if ':' in options['addrport']:
            addr, port = options['addrport'].rsplit(':', 1)
        else:
            addr = '127.0.0.1'
            port = options['addrport']
        
        # WSL2警告の表示
        if addr == '127.0.0.1':
            self.stdout.write(
                self.style.WARNING(
                    '⚠️  サーバーが127.0.0.1でバインドされます\n'
                    '   Windows Chromeからアクセスできません\n'
                    '   WSL2対応するには: python manage.py runserver_wsl'
                )
            )
        elif addr == '0.0.0.0':
            self.stdout.write(
                self.style.SUCCESS(
                    '✅ サーバーが0.0.0.0でバインドされます\n'
                    '  WSL内: http://localhost:8000\n'
                    '  Windows: http://localhost:8000 または http://WSL_IP:8000'
                )
            )
        
        # 親クラスのhandleメソッドを呼び出し
        super().handle(*args, **options)