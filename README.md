# test6

## 概要
FastAPIを使用した簡単な加算APIのプロジェクトです。

## 機能
- `/` - ルートエンドポイント（APIメッセージを返します）
- `/add` - 2つの数値を加算するAPIエンドポイント

## セットアップ

### 必要な環境
- Python 3.8以上

### インストール
```bash
# 依存パッケージのインストール
pip install -r requirements.txt
```

## 使い方

### サーバーの起動
```bash
uvicorn src.main:app --reload
```

サーバーは `http://127.0.0.1:8000` で起動します。

### APIドキュメント
サーバー起動後、以下のURLでAPIドキュメントを確認できます：
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### API使用例
```bash
# 加算APIの使用例
curl -X POST "http://127.0.0.1:8000/add" \
  -H "Content-Type: application/json" \
  -d '{"a": 5, "b": 3}'
```

レスポンス:
```json
{
  "result": 8.0
}
```

## テスト

### テストの実行
```bash
pytest
```

### テストカバレッジ
このプロジェクトには以下のテストが含まれています：
- ルートエンドポイントのテスト
- 正の数の加算テスト
- 負の数の加算テスト
- 正と負の数の混合加算テスト
- 小数の加算テスト
- ゼロの加算テスト

## プロジェクト構造
```
test6/
├── src/
│   └── main.py          # FastAPIアプリケーション
├── test/
│   └── test_main.py     # pytestテストファイル
├── requirements.txt     # 依存パッケージリスト
└── README.md           # このファイル
```

## 開発
このプロジェクトは学習目的で作成されました。