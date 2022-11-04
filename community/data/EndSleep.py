import pandas as pd

data = pd.read_csv('sleep2.csv')
test_df = data[~data['폐업여부'].str.contains('Y')] #페업여부 y는 삭제
test_df =test_df[test_df['업체명'].str.contains('호텔|모텔', na=False)] #호텔과 모텔만 뽑기

# print(test_df['업체명'].value_counts()) 중복확인
test_df = test_df.drop_duplicates(['업체명']) #중복지우기
# print(test_df['업체명'].value_counts()) 지워졌는지 확인

test_df['url'] ='https://cdn.pixabay.com/photo/2018/06/14/21/15/bedroom-3475656_1280.jpg'
df = pd.DataFrame(test_df[["업체명","위도","경도", "url"]])

df.to_csv("sleep.csv", index=False, encoding="utf-8-sig")
# print(test_df)