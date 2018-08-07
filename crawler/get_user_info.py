import time
import random
import argparse

import psycopg2
import numpy as np
import pandas as pd

from functions import twitter

# 済：vaaaaanquish, TJO_datasci, ex_takezawa, arton, tanaka_akr, shin1x1, iteman, shimizukawa, yukihiro_matz, tokibito
# kis, yosuke_furukawa, meso


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help="Target user's screen name")
    args = parser.parse_args()

    target_screen_name = args.target

    tw = twitter()
    ids = tw.getFollowerIds(screen_name=target_screen_name)
    tw.getUserInfo(ids)


if __name__=='__main__':
    main()
