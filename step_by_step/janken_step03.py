""" じゃんけんゲーム step03
勝敗判定の処理を記述する

* パターンを網羅するように記述を増やしていく
* もっと良いプログラムの書き方が思い付くまでは力技でも正しい結果が出れば問題ない
* 本来は不正な値の入力や異常値への対応もこの時点で実装するが今回は正常時の動作の作成を優先し、例外処理は後で実装する
"""
#
# 入力
#

# 0,1,2をキーボードから入力する
print("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー):")

# プレイヤーの手
player_hand = 0  # 変数に代入する値を変更して全てのパターンで正しい結果になるか確認する

#
# 処理
#

# 入力値のチェック 未実装

# コンピュータの手の選択
computer_hand = 1  # チョキが入力されたと仮定する  0,1,2と変更して実行し、表示を確認する

# 勝敗判定
# player_handとcomputer_handをもとに勝敗を判定
# 結果は0:あいこ,1:プレイヤーの勝ち,2:プレイヤーの負け

if player_hand == computer_hand:
    result = 0  # あいこ
elif player_hand == 0 and computer_hand == 1:  # グー vs チョキ
    result = 1  # プレイヤーの勝ち
elif player_hand == 1 and computer_hand == 2:
    result = 1  # プレイヤーの勝ち
elif player_hand == 2 and computer_hand == 0:
    result = 1  # プレイヤーの勝ち
elif player_hand == 0 and computer_hand == 2:  # グー vs パー
    result = 2  # プレイヤーの負け
elif player_hand == 1 and computer_hand == 0:
    result = 2  # プレイヤーの負け
elif player_hand == 2 and computer_hand == 1:
    result = 2  # プレイヤーの負け

#
# 出力
#

hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "あなたの勝ち", "あなたの負け"]

print("あなたの手:", hands[player_hand])  # 入力によって"グー"の部分を切り替える
print("コンピューターの手:", hands[computer_hand])  # ランダムに"チョキ"の部分を切り替える
print(results[result])  # ユーザーの手とコンピューターの手の組合せで表示を切り替える
