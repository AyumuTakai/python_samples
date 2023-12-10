import random
from janken_judge_3_2 import judge

wins = 0  # 勝った回数
for i in range(1, 6):  # iが1〜5の間繰り返す
    print("{0}回目".format(i))  # 回数の表示
    while True:
        player_hand = input("じゃ〜んけ〜ん (0:グー,1:チョキ,2:パー): ")
        try:
            player_hand = int(player_hand)
        except:
            player_hand = -1

        computer_hand = random.randint(0, 2)

        result = judge(player_hand, computer_hand)
        if result == 1:  # プレイヤーの勝ちなら
            wins += 1  # 勝ち数を増やす

        if result >= 0:
            hands = ["グー", "チョキ", "パー"]
            results = ["あいこ", "あなたの勝ち", "あなたの負け"]

            print("あなたの手: ", hands[player_hand])
            print("コンピューターの手: ", hands[computer_hand])
            print(results[result])
            if result > 0:
                break
        else:
            print(" 0,1,2のいずれかの数字を入力してください")

        print()
    print()  # 何回目の繰り返しかをわかりやすくするために空の行を出力する

print("{0}回勝負して{1}回勝ちました。勝率{2}%です。".format(i, wins, wins * 100 / i))  # 勝率表示
