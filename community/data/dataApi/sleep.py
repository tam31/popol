import  pandas as pd
df1 = pd.read_csv("tmpSleep1.csv", encoding='cp949')



df = pd.DataFrame(df1[["업체명","위도","경도","폐업여부"]])
df.to_csv("tmpSleep2.csv", index=False, encoding='cp949')