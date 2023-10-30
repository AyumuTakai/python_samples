"""
均等な確率のおみくじ
大吉、中吉、小吉、凶をランダムに出力します
"""
import random

omikuji = ["大吉","中吉","小吉","凶"]

print(omikuji[random.randint(0,len(omikuji))])