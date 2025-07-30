# StatVizForge API v2.0 本番環境デプロイメントガイド

## 概要

StatVizForge API v2.0 の本番環境への段階的デプロイメントのための完全なガイドです。Docker Compose を使用したコンテナ化された環境で、高可用性、セキュリティ、監視機能を提供します。

## アーキテクチャ

### コンポーネント構成

```
┌─────────────────────────────────────────────────────────────┐
│                    Load Balancer / CDN                      │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                     Nginx (SSL終端)                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                  Django Application                        │
│                  (Gunicorn + Gevent)                       │
└─────┬───────────────────┼───────────────────────────────┬───┘
      │                   │                               │
┌─────▼────┐        ┌─────▼──────┐              ┌────────▼────┐
│PostgreSQL│        │   Redis    │              │ JupyterLab  │
│(Primary) │        │ (Cache +   │              │ (Optional)  │
│          │        │ Sessions)  │              │             │
└──────────┘        └────────────┘              └─────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    監視システム                              │
│  ┌────────────┐  ┌─────────────┐  ┌─────────────────────┐   │
│  │Prometheus  │  │  Grafana    │  │   ヘルスチェック     │   │
│  │(メトリクス) │  │ (可視化)    │  │                     │   │
│  └────────────┘  └─────────────┘  └─────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 クイックスタート

### 1. 前提条件

- **OS**: Ubuntu 20.04 LTS 以上 / CentOS 8 以上
- **Docker**: 20.10 以上
- **Docker Compose**: 2.0 以上
- **メモリ**: 最低 4GB (推奨 8GB)
- **ストレージ**: 最低 20GB (推奨 100GB)
- **CPU**: 最低 2コア (推奨 4コア)

### 2. 環境設定

```bash
# リポジトリをクローン
git clone https://github.com/your-org/StatVizForge_JikkenPy.git
cd StatVizForge_JikkenPy/deployment

# 環境設定ファイルを作成
cp .env.example .env

# 環境設定ファイルを編集
nano .env
```

### 3. 必須設定項目

`.env` ファイルで以下の項目を必ず変更してください：

```bash
# セキュリティ（必須変更）
DJANGO_SECRET_KEY=your-very-secure-secret-key-change-this-in-production
DB_PASSWORD=your-secure-database-password
REDIS_PASSWORD=your-secure-redis-password
ADMIN_PASSWORD=your-secure-admin-password

# ドメイン設定
ALLOWED_HOSTS=yourdomain.com,*.yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://app.yourdomain.com

# メール設定（エラー通知用）
ADMIN_EMAIL=admin@yourdomain.com
EMAIL_HOST_USER=your-email@yourdomain.com
EMAIL_HOST_PASSWORD=your-email-password
```

### 4. SSL証明書設定

```bash
# SSL証明書ディレクトリを作成
mkdir -p nginx/ssl

# 自己署名証明書（開発用）
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout nginx/ssl/key.pem \
    -out nginx/ssl/cert.pem

# Let's Encrypt（本番用）
# certbot を使用して証明書を取得
```

### 5. デプロイ実行

```bash
# デプロイスクリプトを実行
./deploy.sh deploy
```

## 📋 デプロイメントプロセス

### 段階的デプロイメント

1. **前提条件チェック**
   - Docker/Docker Compose の確認
   - 環境設定ファイルの検証
   - 必要ディレクトリの作成

2. **バックアップ作成**
   - 現在のデータベース状態
   - プロジェクトデータ
   - 設定ファイル

3. **サービス起動順序**
   ```
   PostgreSQL → Redis → Django App → Nginx → 監視サービス
   ```

4. **ヘルスチェック**
   - API エンドポイントの応答確認
   - データベース接続確認
   - システムリソース確認

5. **自動ロールバック**
   - ヘルスチェック失敗時の自動復旧

## 🛠️ 運用コマンド

### デプロイメント関連

```bash
# 通常デプロイ
./deploy.sh deploy

# サービス状態確認
./deploy.sh status

# ログ確認
./deploy.sh logs        # 全サービス
./deploy.sh logs web    # 特定サービス

# サービス再起動
./deploy.sh restart

# サービス停止
./deploy.sh stop

# ロールバック
./deploy.sh rollback
```

### 個別コンテナ操作

```bash
# Django管理コマンド実行
docker compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

# データベース接続
docker compose -f docker-compose.prod.yml exec postgres psql -U statvizforge

# Redis接続
docker compose -f docker-compose.prod.yml exec redis redis-cli
```

## 📊 監視とメトリクス

### アクセス先

- **アプリケーション**: https://yourdomain.com
- **管理画面**: https://yourdomain.com/admin/
- **API**: https://yourdomain.com/api/v1/
- **Grafana**: https://yourdomain.com:3000
- **Prometheus**: https://yourdomain.com:9090

### 主要メトリクス

1. **アプリケーション**
   - レスポンス時間
   - エラー率
   - API呼び出し回数
   - アクティブユーザー数

2. **システム**
   - CPU使用率
   - メモリ使用率
   - ディスク使用率
   - ネットワーク転送量

3. **データベース**
   - 接続数
   - クエリ実行時間
   - デッドロック数
   - テーブルサイズ

## 🔒 セキュリティ

### 実装済みセキュリティ機能

1. **アプリケーション層**
   - ディレクトリトラバーサル攻撃防止
   - 入力値バリデーション
   - レート制限
   - セキュアヘッダー

2. **ネットワーク層**
   - HTTPS強制
   - HSTS設定
   - CORS制限
   - CSP設定

3. **データ層**
   - データベース暗号化
   - セッション暗号化
   - パスワードハッシュ化

### セキュリティチェックリスト

- [ ] SSL証明書の有効性確認
- [ ] 強力なパスワード設定
- [ ] ファイアウォール設定
- [ ] 定期的なセキュリティアップデート
- [ ] ログ監視の設定
- [ ] バックアップの暗号化

## 🔧 トラブルシューティング

### 一般的な問題

#### 1. サービスが起動しない

```bash
# ログを確認
./deploy.sh logs

# サービス状態確認
docker compose ps

# 個別サービス再起動
docker compose restart web
```

#### 2. データベース接続エラー

```bash
# PostgreSQL状態確認
docker compose exec postgres pg_isready -U statvizforge

# 接続設定確認
docker compose exec web python manage.py dbshell
```

#### 3. SSL証明書エラー

```bash
# 証明書有効性確認
openssl x509 -in nginx/ssl/cert.pem -text -noout

# Nginx設定テスト
docker compose exec nginx nginx -t
```

#### 4. パフォーマンス問題

```bash
# リソース使用量確認
docker stats

# アプリケーションメトリクス確認
curl https://yourdomain.com/api/v1/server-info/
```

### ログファイル

- **アプリケーション**: `/opt/statvizforge/logs/production.log`
- **セキュリティ**: `/opt/statvizforge/logs/security.log`
- **Gunicorn**: `/opt/statvizforge/logs/gunicorn.*.log`
- **Nginx**: `/var/log/nginx/access.log`, `/var/log/nginx/error.log`

## 🔄 アップデート手順

### マイナーアップデート

```bash
# 最新コードを取得
git pull origin main

# 新しいイメージをビルド
docker compose build --no-cache

# ローリングアップデート
./deploy.sh deploy
```

### メジャーアップデート

```bash
# 手動バックアップ
./deploy.sh backup

# マイグレーション確認
./deploy.sh migrate --dry-run

# アップデート実行
./deploy.sh deploy

# ロールバック準備
./deploy.sh rollback  # 問題がある場合
```

## 📈 スケーリング

### 水平スケーリング

```yaml
# docker-compose.prod.yml
web:
  deploy:
    replicas: 3  # アプリケーションサーバーを3つに増加
```

### 垂直スケーリング

```yaml
# リソース制限の調整
web:
  deploy:
    resources:
      limits:
        memory: 2G
        cpus: '1.0'
```

## 🚨 災害復旧

### バックアップ戦略

1. **日次自動バックアップ**
   - データベース完全バックアップ
   - プロジェクトファイル
   - 設定ファイル

2. **リアルタイム同期**
   - データベースレプリケーション
   - ファイル同期（rsync/AWS S3）

3. **災害復旧手順**
   ```bash
   # バックアップからの復旧
   ./deploy.sh restore --backup-date=2025-01-30
   
   # データ整合性チェック
   ./deploy.sh verify
   ```

## 📞 サポート

### 緊急時連絡先

- **技術責任者**: tech-lead@yourdomain.com
- **運用責任者**: ops@yourdomain.com
- **24時間サポート**: +81-XX-XXXX-XXXX

### ドキュメント

- **API仕様書**: `/doc/APIja.md`
- **テスト結果**: `/testing/results/`
- **アーキテクチャ図**: `/doc/architecture/`

---

**注意**: このドキュメントは本番環境の運用を想定しています。本番環境にデプロイする前に、必ずステージング環境での十分なテストを実施してください。