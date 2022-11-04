import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from community.recommend.restaurant import recommend_eat
from community.recommend.recommend_tag import recommend
from community.recommend.stay import recommend_stay

def plan(start_time, total_date, s):
    date = 0
    tour = recommend(total_date*2, s)
    eat_name=[]
    total = []
    next = 0
    print(1)
    while date != total_date:
        if start_time >= 18:
            re_total = {
                "name": tour[next][0],
                'Latitude': tour[next][1],
                'Lognitude': tour[next][2],
                'url': tour[next][3]

            }
            total.append(re_total)

            # 숙소
            stay = recommend_stay(tour[next])

            re_total = {
                "name": stay[0],
                'Latitude': stay[1],
                'Lognitude': stay[2],
                'url': stay[3]
            }

            total.append(re_total)

            next+=1
            start_time = 9
            date += 1
            continue
        else:
            if start_time <12:
                re_total = {
                    "name": tour[next][0],
                    'Latitude': tour[next][1],
                    'Lognitude': tour[next][2],
                    'url': tour[next][3]

                }
                total.append(re_total)


                data2 = tour[next]
                re_eat = recommend_eat(data2, eat_name)

                re_total = {
                    "name": re_eat[0],
                    'Latitude': re_eat[1],
                    'Lognitude': re_eat[2],
                    'url': re_eat[3]
                }
                eat_name.append(re_eat[0])
                total.append(re_total)

                next +=1
                start_time = 14

            if start_time >=12 and start_time <14 :

                data2 = tour[next]
                re_eat = recommend_eat(data2, eat_name)

                re_total = {
                    "name": re_eat[0],
                    'Latitude': re_eat[1],
                    'Lognitude': re_eat[2],
                    'url': re_eat[3]
                }
                eat_name.append(re_eat[0])
                total.append(re_total)
                start_time  = 14

            if start_time >=14 and start_time <18:
                re_total = {
                    "name": tour[next][0],
                    'Latitude': tour[next][1],
                    'Lognitude': tour[next][2],
                    'url': tour[next][3]

                }
                total.append(re_total)

                data2 = tour[next]
                re_eat = recommend_eat(data2, eat_name)

                re_total = {
                    "name": re_eat[0],
                    'Latitude': re_eat[1],
                    'Lognitude': re_eat[2],
                    'url': re_eat[3]
                }
                eat_name.append(re_eat[0])
                total.append(re_total)

                stay = recommend_stay(tour[next])
                re_total = {
                    "name": stay[0],
                    'Latitude': stay[1],
                    'Lognitude': stay[2],
                    'url': stay[3]
                }

                total.append(re_total)
                next += 1
                start_time = 9
            date+=1
    return total
#
# print(plan(20, 2, '바다'))