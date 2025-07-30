#!/bin/bash
set -e

echo "Starting StatVizForge API v2.0 Production Deployment..."

# データベース接続待機
echo "Waiting for database connection..."
python << END
import os
import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_db():
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            conn = psycopg2.connect(
                host=os.environ.get('DB_HOST', 'postgres'),
                port=os.environ.get('DB_PORT', '5432'),
                user=os.environ.get('DB_USER', 'statvizforge'),
                password=os.environ.get('DB_PASSWORD', ''),
                database=os.environ.get('DB_NAME', 'statvizforge')
            )
            conn.close()
            print("Database connection successful!")
            return True
        except OperationalError:
            retry_count += 1
            print(f"Database connection attempt {retry_count}/{max_retries} failed. Retrying in 2 seconds...")
            time.sleep(2)
    
    print("Failed to connect to database after maximum retries!")
    return False

if not wait_for_db():
    exit(1)
END

# Redis接続待機
echo "Waiting for Redis connection..."
python << END
import os
import time
import redis
from redis import ConnectionError

def wait_for_redis():
    max_retries = 30
    retry_count = 0
    
    redis_url = os.environ.get('REDIS_URL', 'redis://redis:6379/1')
    
    while retry_count < max_retries:
        try:
            r = redis.from_url(redis_url)
            r.ping()
            print("Redis connection successful!")
            return True
        except ConnectionError:
            retry_count += 1
            print(f"Redis connection attempt {retry_count}/{max_retries} failed. Retrying in 2 seconds...")
            time.sleep(2)
    
    print("Failed to connect to Redis after maximum retries!")
    return False

if not wait_for_redis():
    exit(1)
END

# データベースマイグレーション
echo "Running database migrations..."
python manage.py migrate --noinput --settings=config.production_settings

# 静的ファイル収集
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear --settings=config.production_settings

# スーパーユーザー作成（初回のみ）
echo "Creating superuser if not exists..."
python << END
import os
import django
from django.conf import settings
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.production_settings')
django.setup()

User = get_user_model()
admin_email = os.environ.get('ADMIN_EMAIL', 'admin@localhost')
admin_password = os.environ.get('ADMIN_PASSWORD', 'change_this_password')

if not User.objects.filter(email=admin_email).exists():
    User.objects.create_superuser(
        username='admin',
        email=admin_email,
        password=admin_password
    )
    print(f"Superuser created: {admin_email}")
else:
    print("Superuser already exists")
END

# ログディレクトリ作成
mkdir -p /opt/statvizforge/logs

# キャッシュのウォームアップ
echo "Warming up cache..."
python << END
import os
import django
import requests
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.production_settings')
django.setup()

try:
    # 基本的なエンドポイントへのリクエストでキャッシュを準備
    import time
    time.sleep(2)  # サービス起動待機
    
    # 内部ヘルスチェック
    from django.test import Client
    client = Client()
    response = client.get('/api/v1/test/')
    print(f"Cache warmup response: {response.status_code}")
except Exception as e:
    print(f"Cache warmup warning: {e}")
END

# セキュリティチェック
echo "Running security checks..."
python manage.py check --deploy --settings=config.production_settings

# システム状態確認
echo "System status check..."
python << END
import os
import psutil
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.production_settings')
django.setup()

print(f"Python version: {os.sys.version}")
print(f"Django version: {django.get_version()}")
print(f"Memory usage: {psutil.virtual_memory().percent}%")
print(f"Disk usage: {psutil.disk_usage('/').percent}%")
print(f"CPU count: {psutil.cpu_count()}")

# 設定確認
print(f"Debug mode: {settings.DEBUG}")
print(f"Allowed hosts: {settings.ALLOWED_HOSTS}")
print(f"Database engine: {settings.DATABASES['default']['ENGINE']}")
print(f"Cache backend: {settings.CACHES['default']['BACKEND']}")
END

echo "Production environment setup completed successfully!"
echo "Starting application server..."

# メインコマンドを実行
exec "$@"