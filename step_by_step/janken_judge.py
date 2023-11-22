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


if __name__ == "__main__":

    # 勝敗判定関数のテスト
    # 入力値(引数)と結果(戻り値)の組合せが正しいかチェックする
    # 実行した結果何も表示されなければOK

    # あいこのテスト
    if judge(0, 0) != 0:
        print(0, 0, "NG")
    if judge(1, 1) != 0:
        print(1, 1, "NG")
    if judge(2, 2) != 0:
        print(2, 2, "NG")

    # プレイヤー勝ちのテスト
    if judge(0, 1) != 1:
        print(0, 1, "NG")
    if judge(1, 2) != 1:
        print(1, 2, "NG")
    if judge(2, 0) != 1:
        print(2, 0, "NG")

    # プレイヤー負けのテスト
    if judge(0, 2) != 2:
        print(0, 2, "NG")
    if judge(1, 0) != 2:
        print(1, 0, "NG")
    if judge(2, 1) != 2:
        print(2, 1, "NG")

    # 異常値のテスト
    if judge(-1, 1) != -1:
        print(-1, 1, "NG")
    if judge(0, -1) != -1:
        print(0, -1, "NG")
    if judge(-1, -1) != -1:
        print(-1, -1, "NG")
