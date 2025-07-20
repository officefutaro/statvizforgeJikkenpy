#!/bin/bash

# Django REST API環境セットアップスクリプト

echo "Django REST API環境をセットアップします..."

# 仮想環境の作成
echo "1. 仮想環境を作成しています..."
python3 -m venv venv

# 仮想環境の有効化
echo "2. 仮想環境を有効化しています..."
source venv/bin/activate

# pipのアップグレード
echo "3. pipをアップグレードしています..."
python -m pip install --upgrade pip

# Django関連パッケージのインストール
echo "4. Django REST frameworkをインストールしています..."
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install python-decouple

# requirements.txtの作成
echo "5. requirements.txtを作成しています..."
pip freeze > requirements.txt

echo "セットアップが完了しました！"
echo "仮想環境を有効化するには以下のコマンドを実行してください:"
echo "source venv/bin/activate"