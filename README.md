# social_recruiter
## 実行環境
- Python3.5
- Django2.0.6

## 画面
- ログイン
- Twitterユーザリストアップ
- 設定

## DB
- Engineer_DB
    - user_id
    - ユーザ名
    - 自己紹介
    - フォロー数
    - フォロワー数

- Follower_DB    
    - user_id

- Config_DB    
    - サービス利用者名
    - 会社名？
    - DM定型文
    - 検索ワード

## EC2環境で実行
gunicorn your_project.wsgi --bind=0.0.0.0:8000 -D

## TODO
- アカウント情報入力時、求人情報も
- フロントでのみID１から
- 位置情報カラムに追加
- follow follower いる？表示形式検討
- 高速化
  - redis
  - サーバ増やすか..?
- 類似度
  - COS類似度とか
  - 何で文字列を定量化するかは検討
