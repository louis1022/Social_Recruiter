# エンジニア採用Bot
<<<<<<< HEAD
-----

## やること
- Twitterでエンジニアをピックアップする。
- エンジニアの特性を出す(プロフィールやツイートから取得)
  - 有名なエンジニアユーザーから辿るのもありかもしれない
  - wordcloudを使うのはいいかと思った。
  - とりあえず、ユーザーピックアップのところまで完成させら、オファーに必要な要素を再確認し、実装
- 人事は最終的にDMや@でアプローチする。

### 欲しいメソッド
- ユーザー検索（ワード？辿る？）
- ユーザー情報取得
- ユーザーツイート取得
  - 全文繋げて、wordcloudにかけるとか考えてる
  - 他にユーザー特徴を拾えるものがあればやりたい。


## 実行
=======

## 環境構築
```
$ brew install direnv
$ cp .envrc.example .envrc
```
- .envrcに必要な環境変数を記述

## 各スクリプトの概要
### get_user_info.py
- あるユーザーのフォロワーの情報を取得するプログラム。  
- 情報の詳細は、`psql_save.insert_user_info`に従う。  
- 実行方保  
```
$ python crawler/get_user_info.py -t tokoroten
```




## PsotgreSQL実行
>>>>>>> 2069cbd52b09fde5cc6420d243cfe6e9821d0875
- Postgresqlの起動
```
postgres -D /usr/local/var/postgres
```

- Postgresqlの停止
```
pkill postgres
```
