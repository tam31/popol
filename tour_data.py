import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from community.models import Tour #무조건 os밑으로


with open('community/data/tour.csv', encoding='utf-8') as csv_file_sub_categories: #오픈파일 위치
    rows = csv.reader(csv_file_sub_categories)
    print(rows)
    next(rows, None)
    for row in rows:
        Tour.objects.create(
            name = row[1], #모델 이름에 맞추어 적기
            tourLatitude = row[2],
            tourLongitude = row[3],
            tour_url = row[4],
            visitCnt = row[5]
        )
        print(row)