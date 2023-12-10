"""
じゃんけんゲームの作成
問題1 ヒント3 作例
"""
import random

# 入力
player_hand = input("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー): ")  # プレイヤーの手
player_hand = int(player_hand)  # 入力された文字列を整数に変換

# 処理
computer_hand = random.randint(0, 2)  # コンピュータの手を乱数で選択
result = 1  # 勝敗

# 出力
hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "あなたの勝ち", "あなたの負け"]

print("あなたの手: ", hands[player_hand])
print("コンピューターの手: ", hands[computer_hand])
print(results[result])
