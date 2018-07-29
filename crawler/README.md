# エンジニア採用Bot

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
- Postgresqlの起動
```
postgres -D /usr/local/var/postgres
```

- Postgresqlの停止
```
pkill postgres
```
