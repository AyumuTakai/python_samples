""" じゃんけんゲーム step06
勝敗判定を関数にまとめ、別ファイル(janken_judge.py)に分離する

* 別ファイルを直接実行すると関数の動作テストが行なえるように記述する
* 関数化するにあたって、プレイヤー対コンピューター以外の勝利判定でも使えるように変数名を変更(computer_hand→opponent_hand)
"""
import random
from janken_judge import judge
#
# 入力
#

# プレイヤーの手を0,1,2をキーボードから入力する
player_hand = input("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー):")
try:
    # 入力された文字列を整数に変換する
    player_hand = int(player_hand)
except:
    player_hand = -1  # 整数に変換できない場合は-1

#
# 処理
#

# コンピュータの手の選択
computer_hand = random.randint(0, 2)

# 勝敗判定
# player_handとcomputer_handをもとに勝敗を判定
# 結果は0:あいこ,1:プレイヤーの勝ち,2:プレイヤーの負け -1:異常値
result = judge(player_hand, computer_hand)

#
# 出力
#

hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "あなたの勝ち", "あなたの負け"]

if result > 0:
    # 正常時の表示
    print("あなたの手:", hands[player_hand])
    print("コンピューターの手:", hands[computer_hand])
    print(results[result])
else:
    # エラー時の表示
    print("0,1,2のいずれかで入力してください")
