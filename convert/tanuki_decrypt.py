"""
🦡 たぬき暗号解読器
"たぱたいたそたん"を入力すると"ぱいそん"を出力する、
子供のころに遊んだたぬき暗号を解読するプログラムです。
"""

ciphertext = input("🦡 たぬき暗号文を入力してください:")

plaintext = ciphertext.replace("た", "")

print(plaintext)
