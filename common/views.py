import json

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import DetailView

import community
from common.forms import UserForm
from community.models import *

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            print(username)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def ProfileView(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)

    print(1111, user) #로그인한 ID 확인
    print(len(Schedule.objects.filter(user_id = user).values()))
    if len(Schedule.objects.filter(user_id = user).values()) == 0:
        context = {
            'user': user, #로그인한 ID

        }
    else:
        check = Schedule.objects.filter(user_id = user).values()
    # check = Schedule.objects.filter(user_id = user).values()[0]['schedule'] 이걸로 해야함
        print(22223, check[0]['id']) #여기 고치기 아무것도 없을때 고치기!!

    #여기서부터는 다른거 연습(없애야 함)
        ex = Schedule.objects.filter(id = check[0]['id']).values()
        print(33333, ex[0]['schedule'])
    #
    # ex = json.dumps(list(check))
    # print(3333, ex)

        context = {
            'user': user, #로그인한 ID
            'check': check # count()
            # value()
        }
    print(context)
    return render(request, 'common/profile.html', context)

def recheck(request, pk):
    plans = Schedule.objects.filter(id = pk).values()

    re_plan = plans[0]['schedule']
    print(55555, json.loads(re_plan)[0]) #plans[0]['schedule']
    plan = {
        're' : re_plan,
    }
    print(666666, plan)
    return render(request, 'community/check.html', plan)
