"""
回文チェッカー
入力された文字列が回文か判定します
ひらがな(またはカタカナ)だけで入力する必要があります
"""
text = input("回文をひらがなで入力してください:")

reversed_text = "".join(list(reversed(text)))

if text == reversed_text:
    print(text, "は回文です")
else:
    print(text, "は回文ではありません")
