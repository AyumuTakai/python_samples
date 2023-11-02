import tkinter
import random


S_WIDTH = 800  # ウィンドウ幅
S_HEIGHT = 600  # ウィンドウ高さ

FONT_SIZE = 40
FONT = ('Fixedsys', FONT_SIZE)  # フォント設定
MAX_ROW = 12  # 最大表示行数
MAX_COL = 20  # 最大表示桁数

root = tkinter.Tk()
root.geometry(f'{S_WIDTH}x{S_HEIGHT}')


def title():
    """
    タイトル画面
    Game Startボタンを表示
    """
    # タイトル表示
    title = tkinter.Label(root, text="*** PyBird ***", font=FONT)
    title.place(relx=0.5, rely=0.3, anchor='center')
    # スタートボタン
    button = tkinter.Button(root, text="Game Start", font=FONT)
    button.bind("<ButtonPress-1>",
                lambda ev: [title.destroy(), button.destroy(), gamestart(None)])
    button.place(relx=0.5, rely=0.5, anchor='center')


def gamestart(walls):
    """
    ゲーム開始
    """
    # 背景の表示
    if walls:
        for wall in walls:
            wall.destroy()
        walls.clear()
    else:
        walls = wall_init()

    # キャラクター表示
    pc = tkinter.Label(root, text='>')
    pc.config(font=FONT)
    pc.score = 0
    pc.place(x=FONT_SIZE, y=(S_HEIGHT / 2))

    # Score表示
    score = tkinter.Label(root, text="SCORE : "+str(pc.score))
    score.pack()

    # クリックイベント設定
    root.bind('<ButtonPress-1>', lambda ev: hop(pc, score, walls))
    root.bind('<space>', lambda ev: hop(pc, score, walls))
    # タイマー開始
    root.after(20, lambda: update(pc, score, walls))


def gameover(pc, score, walls):
    """
    ゲームオーバー画面
    """
    # マウスイベントの解除
    root.unbind('<ButtonPress-1>')
    score.destroy()
    # キャラクターの削除
    pc.destroy()
    # GameOver表示
    gameover = tkinter.Label(root, text="Game Over")
    gameover.config(font=FONT)
    gameover.place(relx=0.5, rely=0.4, anchor='center')

    # Score表示
    score = tkinter.Label(root, text="SCORE : "+str((pc.score // 10) * 10))
    score.config(font=FONT)
    score.place(relx=0.5, rely=0.55, anchor='center')

    # Retryボタン表示
    button = tkinter.Button(root, text="Retry")
    button.config(font=FONT)
    button.bind("<ButtonPress-1>",
                lambda ev: [gameover.destroy(), score.destroy(), button.destroy(), gamestart(walls)])
    button.place(relx=0.5, rely=0.65, anchor='center')


def hop(pc, score, walls):
    """
    マウスクリック時の跳ねるアクション
    """
    y = pc.winfo_y()
    y -= 20
    if y < 0:
        gameover(pc, score, walls)
        return
    pc.place(y=y)


def update(pc, score, walls):
    """
    画面更新
    """
    y = pc.winfo_y()
    y += 1
    pc_y = y // pc.winfo_height()
    if y > S_HEIGHT:
        gameover(pc, score, walls)
        return
    pc.place(y=y)

    pc.score += 1
    score['text'] = "SCORE : " + str((pc.score // 10) * 10)
    # 障害物スクロールと当たり判定
    for index, wall in enumerate(walls):
        wall_x = wall.winfo_x()

        # 障害物に当ったらゲームオーバー
        print(wall.top, wall.span, pc_y)
        if FONT_SIZE <= wall_x <= FONT_SIZE*2 and not (wall.top <= pc_y < (wall.top + wall.span-1)):
            print('HIT')
            gameover(pc, score, wall)
            return

        # 画面左端に消えたら右側に移動する
        if wall_x <= -wall.winfo_width():

            wall_x += 840
            if index == 0:
                index = len(walls)
            prev = walls[index-1]
            # 前の壁の穴からランダムに穴の位置を上下させる
            # 穴の位置が画面からはみ出さないように制限する
            wall.top = min(MAX_ROW - wall.span-1,
                           max(1, prev.top + random.randint(-1, 1)))
            text = "#\n" * wall.top + "\n" * prev.span + \
                "#\n" * (MAX_ROW - wall.top - prev.span)
            wall['text'] = text

        wall.place(x=wall_x-2)  # 障害物を左に移動する
    root.after(20, lambda: update(pc, score, walls))


def wall_init():
    """
    障害物初期化
    """
    bg_list = []
    x = 0
    span = MAX_ROW // 3
    top = (MAX_ROW - span) // 2
    for i in range(MAX_COL+1):
        text = "#\n" * top + "\n" * span + "#\n" * (MAX_ROW - top - span)
        wall = tkinter.Message(root, text=text)
        wall.config(font=FONT, foreground="gray")
        wall.place(x=x, y=0)
        bg_list.append(wall)
        wall.top = top
        wall.span = span
        x += 40
    return bg_list


# ウィンドウタイトル
root.title('PyBird')
# ウィンドウリサイズ禁止
root.resizable(False, False)
# 画面中央表示
root.update_idletasks()
ww = root.winfo_screenwidth()
lw = root.winfo_width()
wh = root.winfo_screenheight()
lh = root.winfo_height()
root.geometry(str(lw)+"x"+str(lh)+"+" +
              str(int(ww/2-lw/2))+"+"+str(int(wh/2-lh/2)))

# タイトル画面
title()

root.mainloop()
