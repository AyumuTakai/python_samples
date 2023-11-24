"""単語帳
words.txtに保存されている単語を読み込んでランダムに出題
"""
# ファイルパスを操作するための標準ライブラリ
from pathlib import Path
# 乱数を扱うための標準ライブラリ
import random

# 問題データを管理する変数
words = []

# このファイル(__file__=flashcard01.py)と同じフォルダにあるwords.txtのパス
data_path = Path(__file__).parent / "words.txt"
# データファイルを読み込みモードで開く
with open(data_path, mode="r", encoding="utf-8") as f:
    # 1行ずつ処理する
    for line in f.readlines():
        # 文字列中の":"で分割して["問題","答え"]のリストにし、問題リストに追加する
        words.append(line.strip().split(":"))

# データの順番をシャッフル
random.shuffle(words)

# 10問もしくは収録問題数の少ないほうになるまで繰り返す
n = min(10, len(words))
print(n, "問出題します")
for i in range(n):
    # 問題の表示
    print(words[i][0], "?")
    # 解答の入力
    ans = input()
    # 正誤判定と結果の出力
    if ans == words[i][1]:
        print("正解!")
    else:
        print("不正解...")
