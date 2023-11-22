""" じゃんけんゲーム step05
不正な値が入力された場合の対策を行なう

* 例外処理をおこなうか、条件分岐でおこなうかの使い分けが重要
* 正常値が正の数に限られる場合、異常値を表わすために負の数を使うことが多い
"""
import random
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

# 入力値のチェック
if 0 <= player_hand <= 2 and 0 <= computer_hand <= 2:
    # 入力値が0,1,2のときだけ勝敗判定をおこなう

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
else:
    result = -1  # 入力が正しくなかった場合は -1
#
# 出力
#

hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "あなたの勝ち", "あなたの負け"]

if result > 0:
    # 正常時の表示
    print("あなたの手:", hands[player_hand])  # 入力によって"グー"の部分を切り替える
    print("コンピューターの手:", hands[computer_hand])  # ランダムに"チョキ"の部分を切り替える
    print(results[result])  # ユーザーの手とコンピューターの手の組合せで表示を切り替える
else:
    # エラー時の表示
    print("0,1,2のいずれかで入力してください")
