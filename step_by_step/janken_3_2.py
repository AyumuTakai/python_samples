"""
じゃんけんゲームの作成
問題3 ヒント2 作例
"""
import random
from janken_judge_3_2 import judge  # 分割したファイルから関数をインポートする

# 入力
player_hand = input("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー): ")
try:
    player_hand = int(player_hand)
except:
    player_hand = -1

# 処理
computer_hand = random.randint(0, 2)

result = judge(player_hand, computer_hand)  # 勝敗判定関数の呼び出し

# 出力
if result >= 0:
    hands = ["グー", "チョキ", "パー"]
    results = ["あいこ", "あなたの勝ち", "あなたの負け"]

    print("あなたの手: ", hands[player_hand])
    print("コンピューターの手: ", hands[computer_hand])
    print(results[result])
else:
    print(" 0,1,2のいずれかの数字を入力してください")
