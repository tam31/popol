import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from community.models import *


def recommend(s):
    tourList = pd.DataFrame(Tour.objects.values_list('name', 'tag__name'), columns=['name', 'tag'])
    tourList = tourList.groupby(['name'])['tag'].apply(','.join).reset_index()
    tag = pd.DataFrame([('test', s)], columns=tourList.columns)
    tourList = pd.concat([tourList, tag])

    counter_vector = CountVectorizer(ngram_range=(1, 3))
    c_vector_tags = counter_vector.fit_transform(tourList['tag'])

    similarity_tag = cosine_similarity(c_vector_tags, c_vector_tags)
    similarity_tag = pd.DataFrame(similarity_tag, index=tourList['name'], columns=tourList['name'])

    def get_content_based_collabor(tag):
        tourList = similarity_tag[tag].sort_values(ascending=False)[:].reset_index()
        tourListVisit = pd.DataFrame(Tour.objects.values_list('name', 'visitCnt', 'tourLatitude', 'tourLongitude','tour_url'),
                                     columns=['name', 'visit', 'tourLatitude', 'tourLongitude', 'url'])
        tourList = tourList.merge(tourListVisit, on="name", how='inner')
        # tourList = tourList.sort_values(by=[tourList.columns[1]], ascending=False)
        # print(tourList)  # 발표할때 추천자료
        # print()
        tourList = tourList.sort_values(by=[tourList.columns[1], tourList.columns[2]], ascending=False)
        # print(tourList)#발표할때 추천자료
        #첫번쨰 관광지와 가까운순 이걸로 할꺼면 tour_url, url 뺴기
        '''
        List = pd.DataFrame(Tour.objects.values_list('name', 'tourLatitude', 'tourLongitude', 'visitCnt', 'tour_url'),
                            columns=['name', 'tourLatitude', 'tourLongitude', 'visitCnt', 'url'])
        re1 = tourList.iloc[0]
        data1 = [re1[0], re1[3], re1[4]]
        List['add1'] = abs(List['tourLatitude'] - data1[1])
        List['add2'] = abs(List['tourLongitude'] - data1[2])
        List['add3'] = List['add1'] + List['add2']
        List = List.sort_values(List.columns[7])[:10]
        # print(List)

        data1 = []
        for i in range(num):
            re1 = List.iloc[i]
            first = [re1[0], re1[1], re1[2], re1[4]]
            data1.append(first)
        # print(data1)
        '''
        #유사도 순
        # print('tourList')
        # print(tourList)
        data1 = []
        for i in range(len(tourList)):
            re1 = tourList.iloc[i]
            data2 = {
                'name': re1[0],
                'lat': float(re1[3]),
                'lon': float(re1[4]),
                'url': re1[5],
                'vis': int(re1[2])
            }
            data1.append(data2)
        return data1

    return get_content_based_collabor('test')

# print(recommend(2,'바다'))

