import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from community.models import *

def recommend_eat(data2, array):
    List = pd.DataFrame(Restaurant.objects.values_list('name', 'restaurantLatitude', 'restaurantLognitude', 'visitCnt', 'restaurant_url'), columns=['name','restaurantLatitude' ,'restaurantLognitude', 'visitCnt', 'url'])
    # 음식점과 관광지간의 위치계산
    List['add1'] =abs(List['restaurantLatitude']- data2[1])
    List['add2'] =abs(List['restaurantLognitude']- data2[2])
    List['add3'] = List['add1']+List['add2']
    List = List.drop(List.columns[[5, 6]], axis=1)

    if len(array)>0:
        a = ''
        for i in range(len(array)):
            if '(' in array[i]:
                index = array[i].find('(')
                array[i] = array[i][:index]

            if i != len(array) - 1:
                a += array[i] +'|'
            else:
                a+= array[i]

        List = List[~List['name'].str.contains(a)]  # 중복식당 확인

    List = List.sort_values(List.columns[5])[:5]  # 가까운순으로 5개의 식당 추출
    List = List.sort_values(by=[List.columns[3], List.columns[5]], ascending=[False, True])  # 방문순
    row_1 = List.iloc[0]
    first = [row_1[0], row_1[1], row_1[2], row_1[4]]

    return first

# print(recommend_eat(['가덕도 연대봉', 35.026875, 128.83395, 'https://www.visitbusan.net/uploadImgs/files/cntnts/20191231180337567_thumbL'], 0))