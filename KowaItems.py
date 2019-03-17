import pandas as pd


df = pd.read_excel('data/3.15_製品データベース.xlsx',encoding="UTF-8")
# print(df.query('cable.str.contains("アルミ")', engine='python'))   # 列名cableにアルミが含まれる行の抽出

# print(df.query('55 <= min1 < 80'))  # 列名min1の数値が範囲が55～80の行の抽出

size1 = 38
size2 = 5
size = (df.query('min1 <= @size1 & max1 >= @size1 & min2 <= @size2 & max2 >= @size2'))

print(size)
