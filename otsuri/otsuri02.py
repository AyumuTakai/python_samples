
"""
お釣りの組合せ計算機 その2
金額を入力すると、一番枚数の少なくなる日本の通貨の組合せを出力します。
紙幣、貨幣の金額をリストで管理します。
"""
amount = int(input("金額を入力してください:"))

# 通貨のリスト
currencies = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]

for currency in currencies:
    if amount >= currency:
        y = amount // currency
        amount = amount % currency
        print(currency, "円", y, "枚")
