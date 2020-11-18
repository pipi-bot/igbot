"""
    instabot example

    Workflow:
        Like last images with hashtag.
"""

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="finahokulani")
parser.add_argument("-p", type=str, help="Star2016")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("hashtags", type=str, nargs="+", help="hashtags")
args = parser.parse_args()

bot = Bot()
bot.login(username=finahokulani.u, password=Star2016.p, proxy=args.proxy)

for hashtag in args.hashtags:
tags=["サロモ","外人風ヘア","海外スタイル","留学","海外留学","海外好きな人と繋がりたい","ハワイ","フラダンス","ハワイアン","タヒチアン","いいね返し","ハイフ","プライベートサロン","エステサロン","ljk","jc","サーフィン","美容学生","高校生","作品撮り","ljc","jk3","フラガール","専門学生","blink"]
wait=25*60# in seconds=> 25 minutes
retry=5*60*60# in hours=> 5hours
    bot.like_hashtag(hashtag)
    
    while True:
try:
for hashtag in tags:
bot.like_hashtag(hashtag)
sleep(wait)
except:
sleep(retry)
