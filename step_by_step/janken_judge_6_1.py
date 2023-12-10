import datetime


def judge(player_hand, opponent_hand):
    """勝敗判定関数"""
    # 入力値のチェック
    if 0 <= player_hand <= 2 and 0 <= opponent_hand <= 2:
        if player_hand == opponent_hand:
            result = 0  # あいこ
        elif player_hand == 0 and opponent_hand == 1:  # グー vs チョキ
            result = 1  # プレイヤーの勝ち
        elif player_hand == 1 and opponent_hand == 2:  # チョキ vs パー
            result = 1  # プレイヤーの勝ち
        elif player_hand == 2 and opponent_hand == 0:  # パー vs グー
            result = 1  # プレイヤーの勝ち
        elif player_hand == 0 and opponent_hand == 2:  # グー vs パー
            result = 2  # プレイヤーの負け
        elif player_hand == 1 and opponent_hand == 0:  # チョキ vs グー
            result = 2  # プレイヤーの負け
        elif player_hand == 2 and opponent_hand == 1:  # パー vs チョキ
            result = 2  # プレイヤーの負け
    else:
        result = -1  # 入力が正しくなかった場合は -1

    return result


def logged_judge(player_hand, computer_hand):
    result = judge(player_hand, computer_hand)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hands = ["グー", "チョキ", "パー"]
    results = ["あいこ", "あなたの勝ち", "あなたの負け"]

    with open("results.csv", mode="a", encoding="utf-8") as f:
        f.write('"{0}",{1},"{2}",{3},"{4}",{5},"{6}"\n'.format(now, player_hand,
                hands[player_hand], computer_hand, hands[computer_hand], result, results[result]))

    return result
