from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import csv
from community.models import Tour
from community.data.crawling.crawlingTag import get_tour_tag

# Create your tests here.
all = Tour.objects.all() #데이터에 있는 tour 데이터를 가져온다
tagAll = list()

for index in all:
    tourName = index.__str__()
    tag = get_tour_tag(tourName)
    tagAll.append(tag)


with open("tag.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(tagAll)