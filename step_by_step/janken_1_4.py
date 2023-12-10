"""
じゃんけんゲームの作成
問題1 ヒント4 作例
"""
import random

# 入力
player_hand = input("じゃ〜んけ〜ん (0:グー, 1:チョキ, 2:パー): ")
player_hand = int(player_hand)

# 処理
computer_hand = random.randint(0, 2)

if player_hand == computer_hand:
    result = 0  # あいこ
elif player_hand == 0 and computer_hand == 1:  # グー vs チョキ
    result = 1  # プレイヤーの勝ち
elif player_hand == 1 and computer_hand == 2:  # チョキ vs パー
    result = 1  # プレイヤーの勝ち
elif player_hand == 2 and computer_hand == 0:  # パー vs グー
    result = 1  # プレイヤーの勝ち
elif player_hand == 0 and computer_hand == 2:  # グー vs パー
    result = 2  # プレイヤーの負け
elif player_hand == 1 and computer_hand == 0:  # チョキ vs グー
    result = 2  # プレイヤーの負け
elif player_hand == 2 and computer_hand == 1:  # パー vs チョキ
    result = 2  # プレイヤーの負け

# 出力
hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "あなたの勝ち", "あなたの負け"]

print("あなたの手: ", hands[player_hand])
print("コンピューターの手: ", hands[computer_hand])
print(results[result])
