"""
じゃんけんゲーム
剰余を使って勝敗判定
"""
import random

player_hand = int(input("じゃ〜んけ〜ん (1:グー, 2:チョキ, 3:パー):")) - 1

computer_hand = random.randint(0, 2)

hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "あなたの勝ち!", "あなたの負け!"]
# 相手の手の数から自分の手の数を引いて3で割った余りを使って勝敗を判定
# 余り0=あいこ、余り1=勝ち,余り2=負け
result = (computer_hand - player_hand) % 3

print("あなたの手", hands[player_hand])
print("コンピューターの手", hands[computer_hand])
print(results[result])
