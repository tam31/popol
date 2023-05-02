import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from community.models import *


def recommend(num, s):
    tourList = pd.DataFrame(Tour.objects.values_list('name', 'tag__name'), columns=['name', 'tag'])
    tourList = tourList.groupby(['name'])['tag'].apply(','.join).reset_index() #각 name별 tag그룹
    tag = pd.DataFrame([('test', s)], columns=tourList.columns) #컬럼명 추출하여 사용자가 선택한 태그와 함께 데이터프레임으로 만들기
    tourList = pd.concat([tourList, tag])

    counter_vector = CountVectorizer(ngram_range=(1, 3)) #단어의 빈도수를 숫자로 표현하기 위해
    c_vector_tags = counter_vector.fit_transform(tourList['tag']) #해당 태그를 행렬로 변환

    similarity_tag = cosine_similarity(c_vector_tags, c_vector_tags) #코사인 유사도 값
    similarity_tag = pd.DataFrame(similarity_tag, index=tourList['name'], columns=tourList['name'])

    def get_content_based_collabor(tag):
        tourList = similarity_tag[tag].sort_values(ascending=False)[:20].reset_index() #태그의 빈도수가 많이 나온 순으로 정렬
        tourListVisit = pd.DataFrame(Tour.objects.values_list('name', 'visitCnt', 'tourLatitude', 'tourLongitude','tour_url'),
                                     columns=['name', 'visit', 'tourLatitude', 'tourLongitude', 'url'])
        tourList = tourList.merge(tourListVisit, on="name", how='inner')

        # 태그의 유사도와 방문자가 높은순으로 정렬
        tourList = tourList.sort_values(by=[tourList.columns[1], tourList.columns[2]], ascending=False)

        #첫번쨰 관광지와 가까운순
        '''
        List = pd.DataFrame(Tour.objects.values_list('name', 'tourLatitude', 'tourLongitude', 'visitCnt', 'tour_url'),
                            columns=['name', 'tourLatitude', 'tourLongitude', 'visitCnt', 'url'])
        re1 = tourList.iloc[0]
        data1 = [re1[0], re1[3], re1[4]]
        List['add1'] = abs(List['tourLatitude'] - data1[1])
        List['add2'] = abs(List['tourLongitude'] - data1[2])
        List['add3'] = List['add1'] + List['add2']
        List = List.sort_values(List.columns[7])[:10]

        data1 = []
        for i in range(num):
            re1 = List.iloc[i]
            first = [re1[0], re1[1], re1[2], re1[4]]
            data1.append(first)
        '''
        #유사도 순
        data1 = []
        for i in range(num):
            re1 = tourList.iloc[i]
            first = [re1[0], re1[3], re1[4], re1[5]]
            data1.append(first)
        return data1

    return get_content_based_collabor('test')


