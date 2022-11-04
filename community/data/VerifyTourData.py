
import pandas as pd

data = pd.read_csv('tour.csv')
names = []
for name in data['1']:
    num = name.find('(')
    if num >0:
        name = name[:num]
    num = name.find('-')
    if num > 0:
        name = name[num+1:]
    num = name.find('/')
    if num > 0:
        name = name[:num]
    num = name.find(',')
    if num > 0:
        name = name[:num]
    num = name.find('&')
    if num > 0:
        name = name[:num]

    names.append(name)
data['1'] = names
data.to_csv("tour.csv", index=False, encoding="utf-8-sig")

