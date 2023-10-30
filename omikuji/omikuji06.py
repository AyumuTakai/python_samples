"""
テストコードを含む詳細なおみくじ
大吉、中吉、小吉、凶をランダムに出力します
おみくじの詳細な内容も出力します
御神籤の結果をテストするコードを含んでいます
"""
import random


def omikuji(index):
    """
    おみくじを引き、結果の辞書を返す

    Args:
        index (int): おみくじの結果を決定する数 1〜100

    Returns:
        おみくじの結果の辞書 {"name","rate","field":{"願望","恋愛","学問"}} もしくは None
    """
    # 範囲外の値
    if index < 1 or 100 < index:
        return None
    # おみくじの結果リスト
    # 以下の確率(rate)は合計が100になるようにしてください
    omikuji_list = [
        {"name": "大吉", "rate": 20, "field": {
            "願望": "多く望まなければかなう", "恋愛": "良い人は近くにいる", "学問": "努力は実る"}},
        {"name": "中吉", "rate": 40, "field": {
            "願望": "叶うまでまて", "恋愛": "迷うべからず", "学問": "疲れたときには休め"}},
        {"name": "小吉", "rate": 30, "field": {
            "願望": "かならずかなう", "恋愛": "目移りは避けよ", "学問": "伸びる時期"}},
        {"name": "凶", "rate": 10, "field": {
            "願望": "立ち止まって見直せ", "恋愛": "あせるべからず", "学問": "集中して臨め"}}
    ]
    # 確率の累計
    rate_sum = 0
    # 確率の累計が乱数以上になるまで繰り返す
    for result in omikuji_list:
        rate_sum += result["rate"]
        if index <= rate_sum:
            return result


def print_omikuji():
    """
    おみくじの結果を表示する
    """
    # 1〜100の乱数を得る
    index = random.randint(1, 100)
    result = omikuji(index)
    print("==", result["name"], "==")
    print("願望", result["field"]["願望"])
    print("恋愛", result["field"]["恋愛"])
    print("学問", result["field"]["学問"])


if __name__ == "__main__":
    # omikuji関数のテスト
    assert omikuji(0) == None, "0以下はNoneになるはずが" + str(omikuji(0))
    assert omikuji(1)["name"] == "大吉", "1は大吉になるはずが" + omikuji(1)
    assert omikuji(20)["name"] == "大吉", "20は大吉になるはずが" + omikuji(20)
    assert omikuji(21)["name"] == "中吉", "21は中吉になるはずが" + omikuji(21)
    assert omikuji(60)["name"] == "中吉", "60は中吉になるはずが" + omikuji(60)
    assert omikuji(61)["name"] == "小吉", "61は小吉になるはずが" + omikuji(61)
    assert omikuji(90)["name"] == "小吉", "90は小吉になるはずが" + omikuji(90)
    assert omikuji(91)["name"] == "凶", "91は凶になるはずが" + omikuji(91)
    assert omikuji(100)["name"] == "凶", "100は凶になるはずが" + omikuji(100)
    assert omikuji(101) == None, "101以上はNoneになるはずが" + str(omikuji(101))
    # print_omikuji関数を実行
    print_omikuji()
