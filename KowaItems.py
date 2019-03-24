'''
参考サイト
https://note.nkmk.me/python-pandas-query/
'''

import pandas as pd


df = pd.read_excel('data/3.20_製品データベース.xlsx',encoding="UTF-8")
# print(df.query('cable.str.contains("アルミ")', engine='python'))   # 列名cableにアルミが含まれる行の抽出

# print(df.query('55 <= min1 < 80'))  # 列名min1の数値が範囲が55～80の行の抽出

'''
列名min1がsize1以下　かつ　列名max1がsize1以上
列名min2がsize2以下　かつ　列名max1がsize2以上
列名cableにアルミが含まれる
この３つの条件で、size1（本線）とsize2（分岐線）の組み合わせが使えるアルミ線用の製品を抽出
'''

size1 = 60
size2 = 38
cable = 'アルミ'

size = (df.query('min1 <= @size1 & max1 >= @size1 & min2 <= @size2 & max2 >= @size2'))
print(size.query('cable.str.contains(@cable)', engine='python'))


'''
空白な変数がある場合はその絞り込みを無効にする。ってしたい
'''
