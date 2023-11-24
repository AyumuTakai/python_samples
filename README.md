# python_samples

Python 初級者向けのサンプルプログラム集

Java 版は[こちら](https://github.com/AyumuTakai/java_samples)

## プログラム開発の進め方 (/step_by_step)

じゃんけんゲームを例に、プログラム開発の際にどのような手順や考え方で設計し実装するのか、
段階的にプログラム実装する流れをまとめました。

人によって開発の流れ、順番や考え方は異なります。
この手順だけが正解のように扱わず、あくまで一つの例として扱ってください。

| ステップ | ファイル名 | 概要 |
|--------|-----------|-----|
|01| [janken_step01.py](https://github.com/AyumuTakai/python_samples/blob/main/step_by_step/janken_step01.py)|ランダムな要素や条件分岐などの処理はせず、まずは仮の表示で実行時のイメージを固める|
|02| [janken_step02.py](https://github.com/AyumuTakai/python_samples/blob/main/step_by_step/janken_step02.py)|出力の切り替え処理を記述する|
|03| [janken_step03.py](https://github.com/AyumuTakai/python_samples/blob/main/step_by_step/janken_step03.py)|勝敗判定の処理を記述する|
|04| [janken_step04.py](https://github.com/AyumuTakai/python_samples/blob/main/step_by_step/janken_step04.py)|プレイヤーの手をキーボードから入力し、ランダムなコンピューターの手と勝負できるようにする|
|05| [janken_step05.py](https://github.com/AyumuTakai/python_samples/blob/main/step_by_step/janken_step05.py)|不正な値が入力された場合の対策を行なう|
|06| [janken_step06.py](https://github.com/AyumuTakai/python_samples/blob/main/step_by_step/janken_step06.py), [janken_judge.py](https://github.com/AyumuTakai/python_samples/blob/main/step_by_step/janken_judge.py)|勝敗判定を関数にまとめ、別ファイルに分離する|

### プログラミングの前に

プログラムを何も考えずにいきなり書きだすことはできません。
プログラム言語の文法だけ覚えても実用的なプログラムを作ることは難しいでしょう。
明文化するかどうかは別として、プログラムを書き出すまえに要件定義や設計といった工程をおこなってプログラムの仕様を明確にします。

小さなプログラムを作成する際の設計の例を"[プログラムの設計.pdf](https://github.com/AyumuTakai/python_samples/blob/main/step_by_step/プログラムの設計.pdf)"にまとめてあります。
プログラム開発に慣れてくると頭の中だけで設計をある程度まとめられるようになります。

## 変換/暗号 (/convert)

| 難易度 | ファイル名                                                                                                | 概要             | キーワード                       |
| ------ | --------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------- |
| ☆      | [tanuki_decrypt.py](https://github.com/AyumuTakai/python_samples/blob/main/convert/tanuki_decrypt.py)     | たぬき暗号解読器 | replace,input                    |
| ☆☆     | [palindrome_check.py](https://github.com/AyumuTakai/python_samples/blob/main/convert/palindrome_check.py) | 回文チェッカー   | reversed,list,join,if-else,input |

## さいころ (/dice)

| 難易度 | ファイル名                                                                         | 概要                                        | キーワード             |
| ------ | ---------------------------------------------------------------------------------- | ------------------------------------------- | ---------------------- |
| ☆      | [dice01.py](https://github.com/AyumuTakai/python_samples/blob/main/dice/dice01.py) | 単純なさいころ                              | random                 |
| ☆☆     | [dice02.py](https://github.com/AyumuTakai/python_samples/blob/main/dice/dice02.py) | 振る回数を指定できるさいころ                | random,input,int,while |
| ☆☆     | [dice03.py](https://github.com/AyumuTakai/python_samples/blob/main/dice/dice03.py) | 振る回数を指定でき,合計値も表示するさいころ | random,input,int,while |

## おみくじ (/omikuji)

| 難易度 | ファイル名                                                                                  | 概要                                       | キーワード                                                                       |
| ------ | ------------------------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------- |
| ☆      | [omikuji01.py](https://github.com/AyumuTakai/python_samples/blob/main/omikuji/omikuji01.py) | 均等な確率のおみくじ                       | random,リスト,len 関数                                                           |
| ☆      | [omikuji02.py](https://github.com/AyumuTakai/python_samples/blob/main/omikuji/omikuji02.py) | 確率の異なるおみくじ その 1                | random,リスト,len 関数                                                           |
| ☆☆☆    | [omikuji03.py](https://github.com/AyumuTakai/python_samples/blob/main/omikuji/omikuji03.py) | 確率の異なるおみくじ その 2                | random,リスト,if,for in,break                                                    |
| ☆☆☆    | [omikuji04.py](https://github.com/AyumuTakai/python_samples/blob/main/omikuji/omikuji04.py) | 詳細なおみくじ                             | random,リスト,辞書,if,for in,break                                               |
| ☆☆☆☆   | [omikuji05.py](https://github.com/AyumuTakai/python_samples/blob/main/omikuji/omikuji05.py) | 関数化した詳細なおみくじ                   | 関数,random,リスト,辞書,if,for in,break                                          |
| ☆☆☆☆☆  | [omikuji06.py](https://github.com/AyumuTakai/python_samples/blob/main/omikuji/omikuji06.py) | テストコードを含む詳細なおみくじ           | モジュール,\_\_name\_\_,assert,関数,random,リスト,辞書,if,for in                 |
| ☆☆☆☆☆  | [omikuji07.py](https://github.com/AyumuTakai/python_samples/blob/main/omikuji/omikuji07.py) | ファイルからデータを読み込む詳細なおみくじ | ファイル入力,split,モジュール,\_\_name\_\_,assert,関数,random,リスト,辞書,for in |

## じゃんけん (/janken)

| 難易度 | ファイル名                                                                               | 概要                                    | キーワード                           |
| ------ | ---------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------ |
| ☆☆☆    | [janken01.py](https://github.com/AyumuTakai/python_samples/blob/main/janken/janken01.py) | じゃんけんゲーム 条件分岐による勝敗判定 | random,int,input,リスト,if-elif-else |
| ☆☆☆    | [janken02.py](https://github.com/AyumuTakai/python_samples/blob/main/janken/janken02.py) | じゃんけんゲーム 剰余による勝敗判定     | random,int,input,リスト,剰余         |

## おつりの組合せ (/otsuri)

| 難易度 | ファイル名                                                                               | 概要                        | キーワード                               |
| ------ | ---------------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------- |
| ☆      | [otsuri01.py](https://github.com/AyumuTakai/python_samples/blob/main/otsuri/otsuri01.py) | お釣りの組合せ計算機 その 1 | int,input,if,整数除算,剰余               |
| ☆☆     | [otsuri02.py](https://github.com/AyumuTakai/python_samples/blob/main/otsuri/otsuri02.py) | お釣りの組合せ計算機 その 2 | int,input,if,リスト,for in,整数除算,剰余 |

## 単語帳

| 難易度 | ファイル名                                                                               | 概要                        | キーワード                               |
| ------ | ---------------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------- |
| ☆☆☆   | [flashcard01.py](https://github.com/AyumuTakai/python_samples/blob/main/flashcard/flashcard01.py),[words.txt](https://github.com/AyumuTakai/python_samples/blob/main/flashcard/words.txt) | 単語帳 | input,with,open,Path,\_\_file\_\_,random,リスト,条件分岐|

## Web API の利用 (/webapi)

| 難易度 | ファイル名                                                                                     | 概要                   | キーワード                             |
| ------ | ---------------------------------------------------------------------------------------------- | ---------------------- | -------------------------------------- |
| ☆☆☆☆   | [get_weather.py](https://github.com/AyumuTakai/python_samples/blob/main/webapi/get_weather.py) | 天気予報を取得して表示 | モジュール,request,JSON,datetime,range |
