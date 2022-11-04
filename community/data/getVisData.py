import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import csv
from community.data.UserData import userdata
import pandas as pd

all = pd.read_csv('food2.csv')
count = []
print(all['0'])
for name in all['0']:
    print(name)
    stname = name.__str__()
    vis = userdata(stname)
    count.append(vis)
    print(vis)
print(len(count))
print(count)


# data = pd.read_csv('tour.csv')
all['visit'] = count
all.to_csv('food2.csv', index = False, encoding="utf-8-sig")


'''
관광지 데이터 방문횟수 클로링
all = pd.read_csv('tour.csv')
count = []
print(all['1'])
for name in all['1']:
    print(name)
    stname = name.__str__()
    vis = userdata(stname)
    count.append(vis)
    print(vis)
print(len(count))
print(count)


# data = pd.read_csv('tour.csv')
all['visit'] = count
all.to_csv('tour.csv', index = False, encoding="utf-8-sig")
'''