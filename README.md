# 돌피스

![img](/wiki/main.PNG)
  
- 동아대학교 DAU AI SW Fair Day​:seedling:
- 프로젝트 기간 : `2022.04.01` ~ `2022.09.20`

---- 

## 프로젝트 소개

* 여행 일정 수립에는 평균 10시간 이상걸리는 여러 가지 요소들을 고려하여 계획해야 함.
  - 일정 수립을 위한 정보 획득 문제 : 일정 수립은 기간, 동선, 방문할 관광지와 숙소, 식당 등 여러 가지 정보들을 획득하고 취합해야 함. 관광할 여행지에 대한 정보가 부족한 경우 여행 계획자는 관련 정보 획득의 부담을 느낌.
  - 정보 선별 과정의 비용 문제 : 관광할 여행지들과 식당, 숙소에 대해 정보가 있다 하더라도 계획자는 기간과 동선에 맞게 해당 정보들을 선별하고 일정에 편성해야 함 이러한 과정은 계획자에게 큰 비용을 요구하는 문제가 있음. 

* 추천시스템 기반 여행 일정 생성 웹서비스 개발을 통하여 입력으로 들어온 기간 내 시간의 흐름에 맞게 추천시스템의 방법론을 활용하여 관광지, 식당, 숙소를 편성하는 알고리즘 설계와 이를 모듈화하여 배포하기 위한 웹 사이트 설계 및 구현, 알고리즘에 사용될 기초 데이터 셋 수집을 하고자 한다. 그로인해 계획자로부터 요구되는 부담감을 줄이고 일정계획의 소비 시간을 단축시키고자 목표를 잡았습니다

---- 

## 기술스택
![img](/wiki/stack.PNG)

---- 

## Flow Chart
![img](/wiki/flow.png)

---- 

## 화면 구성 📺
| 메인 페이지  |  일정수정 페이지   |  일정확정 페이지   |
|------|---|---|
| <img width="329" src="https://github.com/tam31/popol/blob/main/wiki/img/11.png"/>   | <img width="329" src="https://github.com/tam31/popol/blob/main/wiki/img/22.png"/> | <img width="329" src="https://github.com/tam31/popol/blob/main/wiki/img/33.png"/>|   
| 여행지간 경로보기   |  마이페이지 확정된 여행일정 저장   |  
| <img width="329" src="https://github.com/tam31/popol/blob/main/wiki/img/44.png"/>   |  <img width="329" src="https://github.com/tam31/popol/blob/main/wiki/img/66.png"/>     |


## 핵심 기능 구현 방법 설명

```
👉 WIKI에 핵심 기능 구현 코드 및 방법 정리
```

[1. 공공데이터api를 가져오기](https://github.com/tam31/popol/wiki/1.1-%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%8F%AC%ED%84%B8%EC%97%90%EC%84%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0)

[2. 숙박데이터 폐업여부 등의 신뢰성검사](https://github.com/tam31/popol/wiki/1.1-%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%8F%AC%ED%84%B8%EC%97%90%EC%84%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0)

[3. 네이버지도 클로링](https://github.com/tam31/popol/wiki/1.3-%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%A7%80%EB%8F%84-%ED%81%B4%EB%A1%9C%EB%A7%81)
