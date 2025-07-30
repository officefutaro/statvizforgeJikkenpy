#!/usr/bin/env python
"""
本番環境用ヘルスチェックスクリプト
コンテナの健全性を監視
"""

import os
import sys
import time
import json
import urllib.request
import urllib.error
from urllib.parse import urljoin

def check_api_endpoint():
    """APIエンドポイントの健全性チェック"""
    base_url = "http://localhost:8000"
    endpoints = [
        "/api/v1/test/",
        "/api/v1/server-info/",
    ]
    
    for endpoint in endpoints:
        url = urljoin(base_url, endpoint)
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    if endpoint == "/api/v1/test/" and data.get('status') == 'ok':
                        continue
                    elif endpoint == "/api/v1/server-info/":
                        continue
                    else:
                        print(f"❌ Endpoint {endpoint} returned unexpected response: {data}")
                        return False
                else:
                    print(f"❌ Endpoint {endpoint} returned status {response.status}")
                    return False
        except urllib.error.URLError as e:
            print(f"❌ Failed to connect to {endpoint}: {e}")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON response from {endpoint}: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error for {endpoint}: {e}")
            return False
    
    return True

def check_database_connection():
    """データベース接続チェック"""
    try:
        import psycopg2
        
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'postgres'),
            port=os.environ.get('DB_PORT', '5432'),
            user=os.environ.get('DB_USER', 'statvizforge'),
            password=os.environ.get('DB_PASSWORD', ''),
            database=os.environ.get('DB_NAME', 'statvizforge')
        )
        
        cursor = cursor = conn.cursor()
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if result and result[0] == 1:
            return True
        else:
            print("❌ Database query returned unexpected result")
            return False
            
    except ImportError:
        print("⚠️  psycopg2 not available, skipping database check")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def check_redis_connection():
    """Redis接続チェック"""
    try:
        import redis
        
        redis_url = os.environ.get('REDIS_URL', 'redis://redis:6379/1')
        r = redis.from_url(redis_url)
        
        # Ping テスト
        if r.ping():
            return True
        else:
            print("❌ Redis ping failed")
            return False
            
    except ImportError:
        print("⚠️  redis not available, skipping Redis check")
        return True
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")
        return False

def check_system_resources():
    """システムリソースチェック"""
    try:
        import psutil
        
        # メモリ使用量
        memory = psutil.virtual_memory()
        if memory.percent > 90:
            print(f"⚠️  High memory usage: {memory.percent}%")
            return False
        
        # ディスク使用量
        disk = psutil.disk_usage('/')
        if disk.percent > 90:
            print(f"⚠️  High disk usage: {disk.percent}%")
            return False
        
        # CPU負荷
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > 95:
            print(f"⚠️  High CPU usage: {cpu_percent}%")
            return False
        
        return True
        
    except ImportError:
        print("⚠️  psutil not available, skipping system resource check")
        return True
    except Exception as e:
        print(f"❌ System resource check failed: {e}")
        return False

def check_log_files():
    """ログファイルの健全性チェック"""
    log_dir = "/opt/statvizforge/logs"
    required_logs = ["production.log", "gunicorn.error.log"]
    
    if not os.path.exists(log_dir):
        print(f"⚠️  Log directory not found: {log_dir}")
        return True  # 初回起動時は存在しない可能性がある
    
    for log_file in required_logs:
        log_path = os.path.join(log_dir, log_file)
        if os.path.exists(log_path):
            # ファイルサイズチェック（異常に大きくないか）
            file_size = os.path.getsize(log_path)
            if file_size > 100 * 1024 * 1024:  # 100MB
                print(f"⚠️  Large log file detected: {log_file} ({file_size / 1024 / 1024:.1f}MB)")
    
    return True

def main():
    """メインヘルスチェック関数"""
    print("🔍 Starting health check...")
    
    checks = [
        ("API Endpoints", check_api_endpoint),
        ("Database Connection", check_database_connection),
        ("Redis Connection", check_redis_connection),
        ("System Resources", check_system_resources),
        ("Log Files", check_log_files),
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        try:
            if check_func():
                print(f"✅ {check_name}: OK")
            else:
                print(f"❌ {check_name}: FAILED")
                all_passed = False
        except Exception as e:
            print(f"❌ {check_name}: ERROR - {e}")
            all_passed = False
    
    if all_passed:
        print("✅ All health checks passed!")
        sys.exit(0)
    else:
        print("❌ Some health checks failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()