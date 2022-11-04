from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #엔터
import webbrowser

# url = "https://map.kakao.com/"
# webbrowser.open(url)

# 브라우저 생성
browser = webdriver.Chrome("C:\chromedriver") #ChromeDriverManager().install()
# 웹사이트 열기
browser.get("https://map.naver.com/v5/search/%ED%95%B4%EC%9A%B4%EB%8C%80%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5")
browser.implicitly_wait(5)#로딩이 끝날때 까지 10초까지는 기다림

x_path = '#_pcmap_list_scroll_container > ul > li > div.Np1CD > div:nth-child(2) > a > div.SbNoJ > div > span.place_bluelink.t3s7S'
search = browser.find_element(By.CSS_SELECTOR, x_path)
search.click()
#browser.find_element(by=By.CSS_SELECTOR, value='span.blind').click()
time.sleep(1)
# #쇼핑 메뉴 클릭
#browser.find_element(by=By.CSS_SELECTOR, value='a.mainmenutab').click()
# browser.find_element(by=By.CSS_SELECTOR, value='a.mainmenutab').click()
# # time.sleep(1)
#
# # #검색창 클릭
# search = browser.find_element(by=By.CSS_SELECTOR, value='input._searchInput_search_input_QXUFf')
# search.click()
# #
# # #검색어 입력
# search.send_keys('아이폰 13')
# search.send_keys(Keys.ENTER)
# #
# # #스크롤 전 높이
# before_h = browser.execute_script("return window.scrollY") #처음 접속할때
#
# #파일생성
#
# #무한 스크롤
# while True:
#     # 맨 아래로 스크롤을 내린다.
#     browser.find_element(by=By.CSS_SELECTOR, value="body").send_keys(Keys.END)
#
#     # 스크롤 사이 페이지 로딩 시간
#     time.sleep(1)
#
#     #스크롤 후 높이
#     after_h = browser.execute_script("return window.scrollY") #처음 접속할때
#
#     if after_h == before_h:
#         break
#     before_h = after_h
#
#
# #여기가 데이터 넣는거
# #상품 정보 div
# items = browser.find_elements(by=By.CSS_SELECTOR, value=".basicList_info_area__17Xyo")
# print(items)
# for item in items:
#     name = item.find_element(by=By.CSS_SELECTOR, value=".basicList_title__3P9Q7").text
#     price = item.find_element(by=By.CSS_SELECTOR, value=".price_num__2WUXn").text
#     link = item.find_element(by=By.CSS_SELECTOR, value=".basicList_title__3P9Q7 > a").get_attribute('href')
#     print(name, price, link)
#     # 데이터쓰기
#
#
# #파일닫기

#
# # try:
# #     name = item.find_element(by=By.CSS_SELECTOR, value=".basicList_title__3P9Q7").text
# # except:
# #     name = "없음"