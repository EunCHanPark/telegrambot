# clien_market_parser.py
import requests
from bs4 import BeautifulSoup
import os
import time
import telegram

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = f"https://api.telegram.org/bot6502198106:AAGGfbeQ3Uvm0yZkr_xua4__9g_MNBAlrnk/sendMessage"

# req = requests.get('https://arca.live/b/hotdeal')
# req.encoding = 'utf-8'
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')

# posts = soup.select('body > div.root-container > div.content-wrapper.clearfix > article > div > div.article-list > div.list-table.hybrid > div:nth-child(4) > div > div > span.vcol.col-id > span')
# latest = posts[0].text
# print(latest)

# new_Post = soup.select('body > div.root-container > div.content-wrapper.clearfix > article > div > div.article-list > div.list-table.hybrid > div:nth-child(4) > div > a')
# print(new_Post[0].attrs['href'])

#새로운 글이 있느지 확인후 있으면 톡 보내기
while True:
    req = requests.get('https://arca.live/b/hotdeal')
    req.encoding = 'utf-8'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('body > div.root-container > div.content-wrapper.clearfix > article > div > div.article-list > div.list-table.hybrid > div:nth-child(4) > div > div > span.vcol.col-id > span')
    latest = posts[0].text
    new_Post = soup.select('body > div.root-container > div.content-wrapper.clearfix > article > div > div.article-list > div.list-table.hybrid > div:nth-child(4) > div > a')

    params = {
    'chat_id': -4079462539,
    'text': 'https://arca.live/'+new_Post[0].attrs['href'],
    }
    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest:
            r = requests.get(url, params=params)
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
        f_write.write(latest)
        f_write.close()

    time.sleep(600)