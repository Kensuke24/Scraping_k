import requests
from bs4 import BeautifulSoup
import re

# 初回のみ
target_url = 'http://kowaelec.jp/product/connect/01.html'
# Requestsを使って、webから取得
r = requests.get(target_url)
# 要素を抽出
soup = BeautifulSoup(r.content, 'lxml')


for td in soup.find_all('td'):
    print(td.getText())




'''
# https://www.yahoo.co.jp/のトップニュース
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for e in elems:
    print(e.getText())
'''

