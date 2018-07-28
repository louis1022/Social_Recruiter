import psycopg2
import time
import random
import numpy as np
import pandas as pd

from functions import twitter

# スキーマ・テーブル定義の宣言（初回実行のみ）
def db_init_setup():
    from db_setup import psql_save
    psql = psql_save()
    psql.recreate_tables()

def get_user_info():
    tw = twitter()
    # 済：vaaaaanquish, TJO_datasci, ex_takezawa,
    #
    target_screen_name = ['tokoroten']
    for t in target_screen_name:
        ids = tw.getFollowerIds(screen_name=t)
        tw.getUserInfo(ids)
        time.sleep(60*10)

def main():
    get_user_info()


if __name__=='__main__':
    main()
