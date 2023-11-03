"""
じゃんけんゲーム
"""
import random

player_hand = int(input("じゃ〜んけ〜ん (1:グー, 2:チョキ, 3:パー):"))

computer_hand = random.randint(1, 3)

hands = ["グー", "チョキ", "パー"]

if player_hand == 1:  # グー
    if computer_hand == 1:
        result = "あいこ"
    elif computer_hand == 2:
        result = "あなたの勝ち!"
    else:
        result = "あなたの負け!"
elif player_hand == 2:  # チョキ
    if computer_hand == 2:
        result = "あいこ"
    elif computer_hand == 3:
        result = "あなたの勝ち!"
    else:
        result = "あなたの負け!"
elif player_hand == 3:  # パー
    if computer_hand == 3:
        result = "あいこ"
    elif computer_hand == 1:
        result = "あなたの勝ち!"
    else:
        result = "あなたの負け!"
else:
    print("1, 2, 3のいずれかの数字を入力してください")
    quit()

print("あなたの手", hands[player_hand-1])
print("コンピューターの手", hands[computer_hand-1])
print(result)
