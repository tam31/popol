# Open API 받기

import requests
url = 'http://apis.data.go.kr/6260000/FoodService/getFoodKr'
params = {'serviceKey': 'Nwzr/rw30wc8e5Fe4BjtZlJL5ZU3IWo4ZH6pcMY8ORMomxrjSCRQWhmLHSnJDu/cYTxodlGz5/72jXSMuodSmQ==',
          'pageNo': '1',
          'numOfRows': '149'}

response = requests.get(url, params=params)
content = response.text

import pandas as pd
import bs4


xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
rows = xml_obj.findAll('item')

columns = rows[0].find_all()
rowList = []
columnList = []
rowsLen = len(rows)

for i in range(0, rowsLen):
    columns = rows[i].find_all()
    columnsLen = len(columns)
    for j in range(0, 1):
        eachColumn = columns[0].text #음식점명
        eachColumn2 = columns[1].text #경도
        eachColumn3 = columns[16].text #위도
        eachColumn4 = columns[4].text #사진
        columnList.append(eachColumn)  # 관광지명
        columnList.append(eachColumn3)  # LAT 위도
        columnList.append(eachColumn2)  # LNG 경도
        columnList.append(eachColumn4)  # 사진
    rowList.append(columnList)
    columnList = []  # 다음 row의 값을 넣기 위해 비워준다.

df_result = pd.DataFrame(rowList)

df_result.to_csv('food.csv' ,encoding='utf-8-sig')
