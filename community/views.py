
from django.core.paginator import Page
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


from .models import *

# Create your views here.
#밑에 부분이 추천
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import date,datetime,time
from community.recommend.algorithm import plan
import json
from community.recommend.tourlist import recommend
# Create your views here.
#



def Home(request):

    return render(request, 'community/home.html')


def Date(request):
    if request.method == 'POST':
        #db 저장할때
        user = Input()
        user.startperiod = request.POST['date']  # input에 name으로 받아야 값을 받을수 있음
        user.endperiod = request.POST['date2']
        user.startime = request.POST['time']
        # user.area = request.POST['local']

        user.save() #데이터에 저장

        tag = request.POST.getlist('tag[]')
        for value in tag:
            if "힐링" in value:
                user.tag.add(Tag.objects.get(name='힐링'))
            if "산책" in value:
                user.tag.add(Tag.objects.get(name='산책'))
            if "공원" in value:
                user.tag.add(Tag.objects.get(name='공원'))
            if "박물관" in value:
                user.tag.add(Tag.objects.get(name='박물관'))
            if "야경" in value:
                user.tag.add(Tag.objects.get(name='야경'))
            if "스포츠" in value:
                user.tag.add(Tag.objects.get(name='스포츠'))
            if "문화" in value:
                user.tag.add(Tag.objects.get(name='문화'))
            if "바다" in value:
                user.tag.add(Tag.objects.get(name='바다'))
            if "사찰" in value:
                user.tag.add(Tag.objects.get(name='사찰'))
            if "사진" in value:
                user.tag.add(Tag.objects.get(name='사진'))

        time = user.startime.split(":")
        start_time = int(time[0])+1
        if int(time[1]) > 30:
            start_time += 1

        start = user.startperiod.split('-')
        end = user.endperiod.split('-')
        date1 = date(int(start[0]), int(start[1]), int(start[2]))
        date2 = date(int(end[0]), int(end[1]), int(end[2]))
        delta = date2 - date1  # 빼기
        num = delta.days

        s = ""
        for i in range(len(tag)):
            s += str(tag[i])
            if i != len(tag) - 1:
                s += " "

        # print(plan(start_time, num, s))
        plans= plan(start_time, num, s)
        dynamicdata = recommend(s)
        # print("성공")

        data={
            'tag' : s,
            'time' : user.startime,
            'day' : user.startperiod,
            'end_day' : user.endperiod,
            'plans' : plans,
            'dyndata': dynamicdata
        }

        # print("여기", data['plans'][0])
        request.session['data'] = data

        return redirect('community:amend')

    else:

        return render(request, 'community/date.html')


def Amend(request):
    if request.method == 'POST':
        # re =[]
        # print(request.method)
        re =request.POST['result']
        # print(re[0])
        data2 = {
            're': re
        }
        # for i in re:
        #     print('end',i)

        request.session['data2'] = data2

        # db 저장할때
        check = Schedule()
        check.user_id = request.POST['user_ID']  # input에 name으로 받아야 값을 받을수 있음
        check.schedule = data2['re']
        check.save()  # 데이터에 저장

        # print()
        # print(1111111, request.POST['user_ID'])
        # print(2222222, data2['re'])
        # print("post 성공")
        return redirect('community:check')
    else:
        # print(request.method)
        data = request.session.get('data')
        # print(data, 11)


        tours = Tour.objects.all()
        eats = Restaurant.objects.all()
        stays = Stay.objects.all()
        # print(tours)
        data['tours'] = tours
        data['posts_js'] = json.dumps([post.json() for post in tours])
        data['eats'] = eats
        data['eats_js'] = json.dumps([eat.json() for eat in eats])
        data['stays'] = stays
        data['stays_js'] = json.dumps([stay.json() for stay in stays])
        # tour= {
        #     'tours': tours,
        #     'posts_js': json.dumps([post.json() for post in tours])
        # }
        # print(data['plans'])
        # print("11")
        return render(request, 'community/amend.html', data)  # data, tourData

def Check(request):
    data2 = request.session.get('data2')
    # print()
    # print(111111, json.loads(data2['re'])[0]['name'])
    ex = json.loads(data2['re'])[0]['name']
    # print(ex)



    for i in json.loads(data2['re']):
        # print(i['name']) #여행확정에 이름 뽑기
        value = i['name']

        re = None
        try:
            re = Tour.objects.get(name=value)
            print('성공')
            re.visitCnt += 1
            re.save()
            # print(Tour.objects.filter(name=value).values())
        except Tour.DoesNotExist:
            try:
                re = Restaurant.objects.get(name=value)
                print('식당성공', re.visitCnt)

                re.visitCnt += 1
                re.save()
                # print(Restaurant.objects.filter(name=value).values())
            except Restaurant.DoesNotExist:
                try :
                    re = Stay.objects.filter(name=value).first() #똑같은 데이터가 겹쳐서 임시해결책
                    print('숙소성공', re.visitCnt)

                    re.visitCnt += 1
                    re.save()
                    # print(Stay.objects.filter(name=value).values())
                except Stay.DoesNotExist:
                    re = None


    return render(request, 'community/check.html', data2)