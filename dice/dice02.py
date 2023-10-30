"""
振る回数を指定できるさいころ
指定された回数、1から6までの整数をランダムに出力します
"""
import random

times = int(input("何回さいころを振りますか?整数で入力してください:"))
i = 0
while i < times:
    n = random.randint(1, 6)
    print(n)
    i += 1
