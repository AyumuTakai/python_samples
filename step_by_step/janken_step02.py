""" じゃんけんゲーム step02
出力の切り替え処理を記述する

* 開発初期の段階では、入力値やランダムな値などは使用せず仮の値で固定したほうが動作確認しやすい
"""
#
# 入力
#

# 0,1,2をキーボードから入力する
print("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー):")  # 仮の表示

# プレイヤーの手
player_hand = 0  # グーが入力されたと仮定する 0,1,2と変更して実行し、表示を確認する

#
# 処理
#

# 入力値のチェック 未実装

# コンピュータの手の選択
computer_hand = 1  # チョキが入力されたと仮定する  0,1,2と変更して実行し、表示を確認する

# 勝敗判定
result = 0  # プレイヤーが勝ったと仮定する resultの値を0,1,2と変更して実行し、表示を確認する

#
# 出力
#

# プレイヤーの手とコンピューターの手を数値で扱うことで、表示を["✊","✌","🖐"]や["Rock","Scissors","Paper"]などに用意に切り替えられる
hands = ["グー", "チョキ", "パー"]
# 同様に勝敗を数値で扱うことで表示方法を文字や画像、音声などに変更することも用意にできる
results = ["あいこ", "あなたの勝ち", "あなたの負け"]

print("あなたの手:", hands[player_hand])
print("コンピューターの手:", hands[computer_hand])
print(results[result])
