"""
テストコードを含む詳細なおみくじ
大吉、中吉、小吉、凶をランダムに出力します
おみくじの詳細な内容も出力します
御神籤の結果をテストするコードを含んでいます
"""
import random


def load_data():
    """
    おみくじデータをファイル(omikuji.data)から読み込む
    データ形式は1行1件でコロン区切り
    名前:確率:願望:恋愛:学問
    """
    with open("omikuji.data", "r", encoding="utf-8") as f:
        data = f.read()
        data = data.split("\n")

    omikuji_list = []

    for d in data:
        item = d.split(":")
        omikuji_list.append({
            "name": item[0],
            "rate": int(item[1]),
            "field": {
                "願望": item[2],
                "恋愛": item[3],
                "学問": item[4]
            }
        })
    return omikuji_list


def omikuji(data, index):
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
    # 確率の累計
    rate_sum = 0
    # 確率の累計が乱数以上になるまで繰り返す
    for result in data:
        rate_sum += result["rate"]
        if index <= rate_sum:
            return result


def print_omikuji(data):
    """
    おみくじの結果を表示する
    """
    # 1〜100の乱数を得る
    index = random.randint(1, 100)
    result = omikuji(data, index)
    print("==", result["name"], "==")
    print("願望", result["field"]["願望"])
    print("恋愛", result["field"]["恋愛"])
    print("学問", result["field"]["学問"])


if __name__ == "__main__":

    # おみくじデータの読み込み
    omikuji_list = load_data()

    # omikuji関数のテスト
    assert omikuji(omikuji_list, 0) == None, "0以下はNoneになるはずが" + \
        str(omikuji(omikuji_list, 0))
    assert omikuji(omikuji_list, 1)[
        "name"] == "大吉", "1は大吉になるはずが" + omikuji(omikuji_list, 1)
    assert omikuji(omikuji_list, 20)[
        "name"] == "大吉", "20は大吉になるはずが" + omikuji(omikuji_list, 20)
    assert omikuji(omikuji_list, 21)[
        "name"] == "中吉", "21は中吉になるはずが" + omikuji(omikuji_list, 21)
    assert omikuji(omikuji_list, 60)[
        "name"] == "中吉", "60は中吉になるはずが" + omikuji(omikuji_list, 60)
    assert omikuji(omikuji_list, 61)[
        "name"] == "小吉", "61は小吉になるはずが" + omikuji(omikuji_list, 61)
    assert omikuji(omikuji_list, 90)[
        "name"] == "小吉", "90は小吉になるはずが" + omikuji(omikuji_list, 90)
    assert omikuji(omikuji_list, 91)[
        "name"] == "凶", "91は凶になるはずが" + omikuji(omikuji_list, 91)
    assert omikuji(omikuji_list, 100)[
        "name"] == "凶", "100は凶になるはずが" + omikuji(omikuji_list, 100)
    assert omikuji(omikuji_list, 101) == None, "101以上はNoneになるはずが" + \
        str(omikuji(omikuji_list, 101))

    # print_omikuji関数を実行
    print_omikuji(omikuji_list)
