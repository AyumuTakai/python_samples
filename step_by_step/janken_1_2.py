"""
じゃんけんゲームの作成
問題1 ヒント2 作例
"""
# 入力
print("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー): 0")
player_hand = 0  # プレイヤーの手

# 処理
computer_hand = 1  # コンピュータの手
result = 1  # 勝敗

# 出力
hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "あなたの勝ち", "あなたの負け"]

print("あなたの手:", hands[player_hand])
print("コンピューターの手:", hands[computer_hand])
print(results[result])
