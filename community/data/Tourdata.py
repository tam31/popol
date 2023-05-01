# Python3 샘플 코드 #


import requests
import pprint

url = 'http://apis.data.go.kr/6260000/AttractionService/getAttractionKr'
params = {'serviceKey': 'Nwzr/rw30wc8e5Fe4BjtZlJL5ZU3IWo4ZH6pcMY8ORMomxrjSCRQWhmLHSnJDu/cYTxodlGz5/72jXSMuodSmQ==',
          'pageNo': '1',
          'numOfRows': '114'}

response = requests.get(url, params=params)
content = response.text

from os import name
import xml.etree.ElementTree as et
import pandas as pd
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote

xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
rows = xml_obj.findAll('item')
# print(rows)
columns = rows[0].find_all()
# print(columns[0].name)
rowList = []
nameList = []
columnList = []

rowsLen = len(rows)
for i in range(0, rowsLen):
    columns = rows[i].find_all()

    columnsLen = len(columns)
    # nameList.append(columns[0].name)
    for j in range(0, 1):
        # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장한다. (어차피 rows[0], rows[1], ... 모두 컬럼헤더는 동일한 값을 가지기 때문에 매번 반복할 필요가 없다.)
        # if i == 0:
        #     nameList.append('관광지명')  # 원래는 columns[0].name으로 JSON의 에트리뷰트 값이 들어갔음
        #     nameList.append('위도')
        #     nameList.append('경도')
        # 컬럼값은 모든 행의 값을 저장해야한다.
        eachColumn = columns[0].text
        eachColumn2 = columns[1].text
        eachColumn3 = columns[19].text
        eachColumn4 = columns[18].text
        columnList.append(eachColumn)  # 관광지명
        columnList.append(eachColumn3)  # LAT 위도
        columnList.append(eachColumn2)  # LNG 경도
        columnList.append(eachColumn4)  # 사진
    rowList.append(columnList)
    columnList = []  # 다음 row의 값을 넣기 위해 비워준다. (매우 중요!!)

df_result = pd.DataFrame(rowList)
#df_result[0] = df_result[0].str.replace(pat=r'[^\w]', repl=r'', regex=True)
print(df_result[0][2])
#print(df_result.loc[1][0], len(df_result))
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

    print(df_result[0][i])
# print(df_result[0][19])
# print(num)
# df_result[0][19] = df_result[0][19][:num] # 인덱스 사이 값 반환
# print(df_result[0][19])
#수정본
df_result.to_csv('json.csv' ,encoding='utf-8-sig')
