"""
振る回数を指定でき、合計も表示するさいころ
指定された回数、1から6までの整数をランダムに出力します
最後に合計値を出力します。
"""
import random

times = int(input("何回さいころを振りますか?整数で入力してください:"))
result = 0
i = 0
while i < times:
    n = random.randint(1, 6)
    print(n)
    result += n
    i += 1

print(times, "回さいころを振った合計は", result)
