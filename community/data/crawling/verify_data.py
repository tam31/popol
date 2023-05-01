import pandas as pd
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from community.models import Tour
from community.models import Tag

''' ------------------------- add tag ------------------------------- '''

with open('tag.csv', newline='') as f:
    reader = csv.reader(f)
    tag = list(reader)

for index in tag:
    print(index[0])
    print(Tour.objects.get(name = index[0]))
    q = Tour.objects.get(name=index[0])

    for value in index[1:]:
        if "힐링" in value:
            q.tag.add(Tag.objects.get(name='힐링'))
        if "산책" in value:
            q.tag.add(Tag.objects.get(name='산책'))
        if "공원" in value:
            q.tag.add(Tag.objects.get(name='공원'))
        if "박물관" in value:
            q.tag.add(Tag.objects.get(name='박물관'))
        if "야경" in value:
            q.tag.add(Tag.objects.get(name='야경'))
        if "스포츠" in value:
            q.tag.add(Tag.objects.get(name='스포츠'))
        if "문화" in value:
            q.tag.add(Tag.objects.get(name='문화'))
        if "바다" in value:
            q.tag.add(Tag.objects.get(name='바다'))
        if "사찰" in value:
            q.tag.add(Tag.objects.get(name='사찰'))
        if "사진" in value:
            q.tag.add(Tag.objects.get(name='사진'))
