# 言語ローカライゼーション用ユーティリティ（4言語対応）

# エラーメッセージの多言語辞書
ERROR_MESSAGES = {
    'VALIDATION_ERROR': {
        'en': 'Invalid input data',
        'ja': '入力データが不正です',
        'zh-cn': '输入数据无效',
        'zh-tw': '輸入資料無效'
    },
    'DUPLICATE_FOLDER': {
        'en': 'A project with this folder name already exists',
        'ja': '同じフォルダ名のプロジェクトが既に存在します',
        'zh-cn': '具有此文件夹名称的项目已存在',
        'zh-tw': '具有此資料夾名稱的專案已存在'
    },
    'INTERNAL_ERROR': {
        'en': 'An unexpected error occurred. Please try again later',
        'ja': '予期しないエラーが発生しました。しばらく経ってから再試行してください',
        'zh-cn': '发生意外错误。请稍后重试',
        'zh-tw': '發生意外錯誤。請稍後重試'
    },
    'PROJECT_NOT_FOUND': {
        'en': 'Project not found',
        'ja': 'プロジェクトが見つかりません',
        'zh-cn': '未找到项目',
        'zh-tw': '未找到專案'
    },
    'FAILED_TO_CREATE_PROJECT': {
        'en': 'Failed to create project',
        'ja': 'プロジェクトの作成に失敗しました',
        'zh-cn': '项目创建失败',
        'zh-tw': '專案建立失敗'
    },
    'FAILED_TO_LOAD_PROJECTS': {
        'en': 'Failed to load projects registry',
        'ja': 'プロジェクト一覧の読み込みに失敗しました',
        'zh-cn': '加载项目注册表失败',
        'zh-tw': '載入專案註冊表失敗'
    },
    'FAILED_TO_UPDATE_PROJECT': {
        'en': 'Failed to update project',
        'ja': 'プロジェクトの更新に失敗しました',
        'zh-cn': '项目更新失败',
        'zh-tw': '專案更新失敗'
    },
    'FAILED_TO_DELETE_PROJECT': {
        'en': 'Failed to delete project',
        'ja': 'プロジェクトの削除に失敗しました',
        'zh-cn': '项目删除失败',
        'zh-tw': '專案刪除失敗'
    },
    'FAILED_TO_ARCHIVE_PROJECT': {
        'en': 'Failed to archive project',
        'ja': 'プロジェクトのアーカイブに失敗しました',
        'zh-cn': '项目归档失败',
        'zh-tw': '專案封存失敗'
    },
    'FAILED_TO_LOAD_DELETED_PROJECTS': {
        'en': 'Failed to load deleted projects',
        'ja': '削除済みプロジェクトの読み込みに失敗しました',
        'zh-cn': '加载已删除项目失败',
        'zh-tw': '載入已刪除專案失敗'
    },
    'NO_DELETED_PROJECTS': {
        'en': 'No deleted projects found',
        'ja': '削除済みプロジェクトが見つかりません',
        'zh-cn': '未找到已删除的项目',
        'zh-tw': '未找到已刪除的專案'
    },
    'DELETED_PROJECT_NOT_FOUND': {
        'en': 'Deleted project not found',
        'ja': '削除済みプロジェクトが見つかりません',
        'zh-cn': '未找到已删除的项目',
        'zh-tw': '未找到已刪除的專案'
    },
    'ARCHIVE_FILE_NOT_FOUND': {
        'en': 'Archive file not found',
        'ja': 'アーカイブファイルが見つかりません',
        'zh-cn': '未找到归档文件',
        'zh-tw': '未找到封存檔案'
    },
    'PROJECT_FOLDER_ALREADY_EXISTS': {
        'en': 'Project folder already exists',
        'ja': 'プロジェクトフォルダが既に存在します',
        'zh-cn': '项目文件夹已存在',
        'zh-tw': '專案資料夾已存在'
    },
    'FAILED_TO_EXTRACT_ARCHIVE': {
        'en': 'Failed to extract archive',
        'ja': 'アーカイブの展開に失敗しました',
        'zh-cn': '解压归档失败',
        'zh-tw': '解壓封存失敗'
    },
    'FAILED_TO_RESTORE_PROJECT': {
        'en': 'Failed to restore project',
        'ja': 'プロジェクトの復元に失敗しました',
        'zh-cn': '恢复项目失败',
        'zh-tw': '復原專案失敗'
    },
    # Git関連エラーメッセージ（新規追加）
    'GIT_OPERATION_FAILED': {
        'en': 'Git operation failed',
        'ja': 'Git操作に失敗しました',
        'zh-cn': 'Git操作失败',
        'zh-tw': 'Git操作失敗'
    },
    'GIT_SYNC_OPERATION_FAILED': {
        'en': 'Git sync operation failed',
        'ja': 'Git同期操作に失敗しました',
        'zh-cn': 'Git同步操作失败',
        'zh-tw': 'Git同步操作失敗'
    },
    'COMMIT_MESSAGE_REQUIRED': {
        'en': 'Commit message is required',
        'ja': 'コミットメッセージが必要です',
        'zh-cn': '需要提交消息',
        'zh-tw': '需要提交訊息'
    },
    'BRANCH_NAME_REQUIRED': {
        'en': 'Branch name is required',
        'ja': 'ブランチ名が必要です',
        'zh-cn': '需要分支名称',
        'zh-tw': '需要分支名稱'
    },
    'GIT_NOT_FOUND': {
        'en': 'Git is not installed',
        'ja': 'Gitがインストールされていません',
        'zh-cn': '未安装Git',
        'zh-tw': '未安裝Git'
    },
    'NOT_A_REPO': {
        'en': 'Not a Git repository',
        'ja': 'Gitリポジトリではありません',
        'zh-cn': '不是Git仓库',
        'zh-tw': '不是Git儲存庫'
    },
    'PROJECT_NOT_FOUND': {
        'en': 'Project not found',
        'ja': 'プロジェクトが見つかりません',
        'zh-cn': '未找到项目',
        'zh-tw': '未找到專案'
    },
    'GIT_LOG_FAILED': {
        'en': 'Failed to get Git log',
        'ja': 'Git履歴の取得に失敗しました',
        'zh-cn': '获取Git日志失败',
        'zh-tw': '取得Git日誌失敗'
    }
}

# フィールドバリデーションメッセージ
FIELD_VALIDATION_MESSAGES = {
    'folder_name': {
        'required': {
            'en': 'This field is required',
            'ja': 'この項目は必須です',
            'zh-cn': '此字段为必填项',
            'zh-tw': '此欄位為必填項'
        },
        'already_exists': {
            'en': 'Folder name already exists',
            'ja': 'フォルダ名が既に存在します',
            'zh-cn': '文件夹名称已存在',
            'zh-tw': '資料夾名稱已存在'
        }
    },
    'project_name': {
        'required': {
            'en': 'This field is required',
            'ja': 'この項目は必須です',
            'zh-cn': '此字段为必填项',
            'zh-tw': '此欄位為必填項'
        },
        'max_length': {
            'en': 'Project name must be 255 characters or less',
            'ja': 'プロジェクト名は255文字以内で入力してください',
            'zh-cn': '项目名称不得超过255个字符',
            'zh-tw': '專案名稱不得超過255個字元'
        }
    },
    'description': {
        'required': {
            'en': 'This field is required',
            'ja': 'この項目は必須です',
            'zh-cn': '此字段为必填项',
            'zh-tw': '此欄位為必填項'
        }
    },
    'commit_message': {
        'required': {
            'en': 'Commit message is required',
            'ja': 'コミットメッセージは必須です',
            'zh-cn': '需要提交消息',
            'zh-tw': '需要提交訊息'
        }
    },
    'branch_name': {
        'required': {
            'en': 'Branch name is required',
            'ja': 'ブランチ名は必須です',
            'zh-cn': '需要分支名称',
            'zh-tw': '需要分支名稱'
        }
    }
}

# サポート言語一覧
SUPPORTED_LANGUAGES = ['en', 'ja', 'zh-cn', 'zh-tw']
DEFAULT_LANGUAGE = 'en'

# 言語の表示名
LANGUAGE_NAMES = {
    'en': 'English',
    'ja': '日本語',
    'zh-cn': '简体中文',
    'zh-tw': '繁體中文'
}

# 後方互換性のための言語マッピング
LANGUAGE_COMPATIBILITY_MAP = {
    'zh': 'zh-cn',  # 既存の 'zh' は簡体中国語とみなす
    'cn': 'zh-cn',
    'tw': 'zh-tw'
}


def get_language_from_request(request):
    """リクエストから言語コードを取得（4言語対応）"""
    # URLパラメータから言語を取得
    lang = request.GET.get('lang', '')
    
    # HTTPヘッダーのAccept-Languageも確認
    if not lang:
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
        if 'zh-TW' in accept_language or 'zh-Hant' in accept_language:
            lang = 'zh-tw'
        elif 'zh-CN' in accept_language or 'zh-Hans' in accept_language:
            lang = 'zh-cn'
        elif 'ja' in accept_language:
            lang = 'ja'
        elif 'en' in accept_language:
            lang = 'en'
    
    # 後方互換性を考慮
    if lang in LANGUAGE_COMPATIBILITY_MAP:
        lang = LANGUAGE_COMPATIBILITY_MAP[lang]
    
    # サポートされている言語かチェック
    return lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE


def get_error_message(error_code, language='en'):
    """エラーコードと言語から適切なエラーメッセージを取得"""
    # 後方互換性を考慮
    if language in LANGUAGE_COMPATIBILITY_MAP:
        language = LANGUAGE_COMPATIBILITY_MAP[language]
    
    if error_code not in ERROR_MESSAGES:
        return ERROR_MESSAGES['INTERNAL_ERROR'].get(language, ERROR_MESSAGES['INTERNAL_ERROR'][DEFAULT_LANGUAGE])
    
    if language not in ERROR_MESSAGES[error_code]:
        language = DEFAULT_LANGUAGE
    
    return ERROR_MESSAGES[error_code][language]


def get_field_validation_message(field_name, validation_type, language='en'):
    """フィールドバリデーションメッセージを取得"""
    # 後方互換性を考慮
    if language in LANGUAGE_COMPATIBILITY_MAP:
        language = LANGUAGE_COMPATIBILITY_MAP[language]
    
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


def get_language_display_name(language_code):
    """言語コードから表示名を取得"""
    return LANGUAGE_NAMES.get(language_code, language_code)


def detect_language_from_region(user_agent=None, ip_address=None):
    """ユーザーエージェントやIPアドレスから言語を推測（将来拡張用）"""
    # 将来的にIPアドレスや地域情報から言語を自動判定する機能のベース
    return DEFAULT_LANGUAGE