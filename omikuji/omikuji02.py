"""
確率の異なるおみくじ
大吉、中吉、小吉、凶をランダムに出力します
中吉、小吉が出やすいおみくじです
"""
import random

omikuji = ["大吉","中吉","中吉","小吉","小吉","凶"]

print(omikuji[random.randint(0,len(omikuji))])