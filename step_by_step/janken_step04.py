""" じゃんけんゲーム step04
プレイヤーの手をキーボードから入力し、ランダムなコンピューターの手と勝負できるようにする
この時点で正しい入力であればじゃんけんゲームが遊べるようになる
"""
import random
#
# 入力
#

# プレイヤーの手を0,1,2をキーボードから入力する
player_hand = input("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー):")
# 入力された文字列を整数に変換する
player_hand = int(player_hand)

#
# 処理
#

# 入力値のチェック 未実装

# コンピュータの手の選択
computer_hand = random.randint(0, 2)

# 勝敗判定
# player_handとcomputer_handをもとに勝敗を判定
# 結果は0:あいこ,1:プレイヤーの勝ち,2:プレイヤーの負け

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

#
# 出力
#

hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "あなたの勝ち", "あなたの負け"]

print("あなたの手:", hands[player_hand])
print("コンピューターの手:", hands[computer_hand])
print(results[result])
