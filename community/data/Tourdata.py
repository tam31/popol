import requests

url = 'http://apis.data.go.kr/6260000/AttractionService/getAttractionKr'
params = {'serviceKey': 'Nwzr/rw30wc8e5Fe4BjtZlJL5ZU3IWo4ZH6pcMY8ORMomxrjSCRQWhmLHSnJDu/cYTxodlGz5/72jXSMuodSmQ==',
          'pageNo': '1',
          'numOfRows': '114'}

response = requests.get(url, params=params)
content = response.text


import pandas as pd
import bs4

xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
rows = xml_obj.findAll('item') #xml 여행지의 데이터 추출

columnList = [] #하나의 관광지의 관광지명, 위도, 경도, 사진을 넣기위해
rowList = [] # columnList의 관광지마다 분리하기 위해
rowsLen = len(rows)

for i in range(0, rowsLen):
    columns = rows[i].find_all()

    columnsLen = len(columns)
    # nameList.append(columns[0].name)
    for j in range(0, 1):
        eachColumn = columns[0].text #관광지명
        eachColumn2 = columns[1].text #경도
        eachColumn3 = columns[19].text #위도
        eachColumn4 = columns[18].text #사진
        columnList.append(eachColumn)  # 관광지명
        columnList.append(eachColumn3)  # LAT 위도
        columnList.append(eachColumn2)  # LNG 경도
        columnList.append(eachColumn4)  # 사진
    rowList.append(columnList)
    columnList = []  # 다음 row의 값을 넣기 위해 비워준다.

df_result = pd.DataFrame(rowList) #Pandas 데이터 프레임 만들기

# 관광지명의 필요없는 단어제거
for i in range(len(df_result)):
    num = df_result[0][i].find('(')
    if num > 0:
        df_result[0][i] = df_result[0][i][:num]
    num = df_result[0][i].find('&')
    if num > 0:
        df_result[0][i] = df_result[0][i][:num]
    num = df_result[0][i].find(',')
    if num > 0:
        df_result[0][i] = df_result[0][i][:num]
    num = df_result[0][i].find('/')
    if num > 0:
        df_result[0][i] = df_result[0][i][:num]

df_result.to_csv('tour.csv' ,encoding='utf-8-sig')
