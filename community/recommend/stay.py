import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from community.models import *

def recommend_stay(data2):
    List = pd.DataFrame(Stay.objects.values_list('name', 'stayLatitude', 'stayLognitude', 'visitCnt','stay_url'), columns=['name','stayLatitude' ,'stayLognitude', 'visitCnt', 'url'])
    List['add1'] =abs(List['stayLatitude']- data2[1])
    List['add2'] =abs(List['stayLognitude']- data2[2])
    List['add3'] = List['add1']+List['add2']
    List = List.drop(List.columns[[5,6]], axis=1)
    List = List.sort_values(List.columns[5])[:5]
    List = List.sort_values(by=[List.columns[3], List.columns[5]],ascending=[False, True]) #방문순
    row_1 = List.iloc[0]
    first = [row_1[0], row_1[1], row_1[2],row_1[4]]
    return first

# print(recommend_stay(['임랑해수욕장', 35.31905, 129.26451, 'https://www.visitbusan.net/uploadImgs/files/cntnts/20191224093809621_thumbL']))