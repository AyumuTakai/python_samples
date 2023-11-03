
"""
お釣りの組合せ計算機  その1
金額を入力すると、一番枚数の少なくなる日本の通貨の組合せを出力します。
"""
amount = int(input("金額を入力してください:"))

if amount >= 10000:
    y10000 = amount // 10000
    amount = amount % 10000
    print("1万円札", y10000, "枚")
if amount >= 5000:
    y5000 = amount // 5000
    amount = amount % 5000
    print("五千円札", y5000, "枚")
if amount >= 2000:
    y2000 = amount // 2000
    amount = amount % 2000
    print("千円札", y2000, "枚")
if amount >= 1000:
    y1000 = amount // 1000
    amount = amount % 1000
    print("千円札", y1000, "枚")
if amount >= 500:
    y500 = amount // 500
    amount = amount % 500
    print("五百円玉", y500, "枚")
if amount >= 100:
    y100 = amount // 100
    amount = amount % 100
    print("百円玉", y100, "枚")
if amount >= 50:
    y50 = amount // 50
    amount = amount % 50
    print("五十円玉", y50, "枚")
if amount >= 10:
    y10 = amount // 10
    amount = amount % 10
    print("十円玉", y10, "枚")
if amount >= 5:
    y5 = amount // 5
    amount = amount % 5
    print("五円玉", y5, "枚")

print("1円玉", amount, "枚")
