"""
天気予報を取得して表示
気象庁のWebサイトから明後日までの天気予報の情報を取得して表示します
"""

# HTTPアクセスのためのパッケージからrequest関数を読み込む
from urllib import request
# JSON形式のデータを扱うためのパッケージを読み込む
import json
# 日付処理のためのパッケージを読み込む
from datetime import datetime

# 気象庁の今日明日明後日の東京の天気予報を取得するURL (毎日05:00に内容更新)
# 130000は東京を表わすコード (解説: https://anko.education/webapi/jma )
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
# 指定したURLにリクエストを送ってレスポンスを取得する
response = request.urlopen(url)
# 取得したデータをJSON形式としてPythonのオブジェクトにする
content = json.loads(response.read().decode('utf8'))
# 取得したデータを整形して表示する
# print(json.dumps(content,indent=2,ensure_ascii=False))

# 受け取ったデータから必要な情報を取り出す

# 天気予報概況
time_defines = content[0]["timeSeries"][0]["timeDefines"]  # 日時のリスト
area = content[0]["timeSeries"][0]["areas"][0]  # 地域別データ
area_name = area["area"]["name"]  # 地域の名称
weathers = area["weathers"]      # 日別天気予報のリスト

# 地域名の表示
print(area_name)
# 今日、明日、明後日の天気予報の表示
for i in range(len(time_defines)):
    # タイムゾーン付き日付文字列(%Y-%m-%dT%H:%M:%S%z)をdatetimeオブジェクトに変換
    dt = datetime.strptime(time_defines[i], "%Y-%m-%dT%H:%M:%S%z")
    # 表示用に書式化(%Y年%m月%d日)して文字列化
    dt_str = dt.strftime("%Y年%m月%d日")
    # 日付と天気予報を表示
    print(dt_str, weathers[i])
