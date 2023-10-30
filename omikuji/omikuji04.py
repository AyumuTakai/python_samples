"""
詳細なおみくじ
大吉、中吉、小吉、凶をランダムに出力します
おみくじの詳細な内容も出力します。
"""
import random

# 以下の確率は合計が100になるようにしてください
omikuji = [
    {"name": "大吉", "rate": 20, "field": {
        "願望": "多く望まなければかなう", "恋愛": "良い人は近くにいる", "学問": "努力は実る"}},
    {"name": "中吉", "rate": 40, "field": {
        "願望": "叶うまでまて", "恋愛": "迷うべからず", "学問": "疲れたときには休め"}},
    {"name": "小吉", "rate": 30, "field": {
        "願望": "かならずかなう", "恋愛": "目移りは避けよ", "学問": "伸びる時期"}},
    {"name": "凶", "rate": 10, "field": {
        "願望": "立ち止まって見直せ", "恋愛": "あせるべからず", "学問": "集中して臨め"}}
]

# 1〜100の乱数を得る
index = random.randint(1, 100)

# 確率の累計
rate_sum = 0

# 確率の累計が乱数以上になるまで繰り返す
for result in omikuji:
    rate_sum += result["rate"]
    if index <= rate_sum:
        print("==", result["name"], "==")
        print("願望", result["field"]["願望"])
        print("恋愛", result["field"]["恋愛"])
        print("学問", result["field"]["学問"])
        break
