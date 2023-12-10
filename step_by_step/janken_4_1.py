import random
from janken_judge_3_2 import judge

while True:  # 無限ループ
    player_hand = input("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー): ")
    try:
        player_hand = int(player_hand)
    except:
        player_hand = -1

    computer_hand = random.randint(0, 2)

    result = judge(player_hand, computer_hand)

    if result >= 0:
        hands = ["グー", "チョキ", "パー"]
        results = ["あいこ", "あなたの勝ち", "あなたの負け"]

        print("あなたの手: ", hands[player_hand])
        print("コンピューターの手: ", hands[computer_hand])
        print(results[result])
        if result > 0:  # 1:勝ち、もしくは2:負けの場合
            break  # 無限ループを終了する
    else:
        print(" 0,1,2のいずれかの数字を入力してください")

    print()  # 繰り返しをわかりやすくするために空の行を出力する
