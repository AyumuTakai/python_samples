"""
詳細なおみくじ
大吉、中吉、小吉、凶をランダムに出力します
おみくじの詳細な内容も出力します。
"""
import random

# 以下の確率は合計が100になるようにしてください
omikuji = [["大吉", 20], ["中吉", 40], ["小吉", 30], ["凶", 10]]


# 1〜100の乱数を得る
index = random.randint(1, 100)

# 確率の累計
rate_sum = 0

# 確率の累計が乱数以上になるまで繰り返す
for result in omikuji:
    rate_sum += result[1]
    if index <= rate_sum:
        print(result[0])
        break
