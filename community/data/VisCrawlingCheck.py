import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #selenium에서 사용할 모듈 import
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome("C:\chromedriver") #selenium 사용에 필요한 chromedriver.exe 파일 경로 지정

driver.get("https://map.naver.com/v5/search/" + '일광해수욕장') #네이버 신 지도
try:
   element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.CLASS_NAME, "input_search"))
   )
finally:
   pass

# search_box = driver.find_element(By.CSS_SELECTOR, ".input_search")
# search_box.send_keys('평안도족발')
# search_box.send_keys(Keys.ENTER) #검색창에 입력

time.sleep(5) #화면 표시 기다리기
frame = driver.find_element(By.CSS_SELECTOR,"iframe#searchIframe") # 프레임 지정하기
driver.switch_to.frame(frame)
time.sleep(1)
#아무것도 없을때

Box = driver.find_elements(By.XPATH, '//*[@id="app-root"]/div/div[2]/div')
# print(1111,len(Box))

if len(Box) == 1:
    print('end', len(Box))


#1개는 바로뜸
firstBox = driver.find_elements(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li')
print(000,len(firstBox))

#여기가 문제
Box = driver.find_elements(By.XPATH, '//*[@id="app-root"]/div/div[1]/div')
print(2222,len(Box))

if len(Box) == 1:
    driver.find_element(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/a/div/div').click()

#여기까지
else:
    if len(firstBox) > 1:
        check = driver.find_elements(By.XPATH,'//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div')
        print(55, len(check)) #div의 갯수 구하기
        if len(check) >=3: #사진이 있고 없고로 갯수가 나뉨
            driver.find_element(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/div[2]/a[1]/div/div').click()
        else:
            driver.find_element(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/div[2]/a[1]/div/div').click()

#프레임 지정 지우기(새로 생긴프레임을위해)
driver.switch_to.default_content()
time.sleep(3)
#새로 생긴 프레임지정
driver.switch_to.frame(driver.find_element(By.ID, 'entryIframe'))
time.sleep(3)

cnt = 0
target = driver.find_elements(By.XPATH,'//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span')
# print(1111,len(target))
#print(driver.find_element(By.XPATH,'//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a').text.split()[0])
if len(target) >= 3: #리뷰가 3개, 2, 1개로 나뉨
    if driver.find_element(By.XPATH,'//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a').text.split()[0] == '방문자리뷰':
        # print(111)
        # print(driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a/em').text)
        # print(driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[3]/a/em').text)
        numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a/em').text
        number=numbers.replace(',','')
        cnt += int(number)
        #print(1,int(number))
        # cnt += int(driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[3]/a/em').text)
        numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[3]/a/em').text
        number = numbers.replace(',', '')
        cnt += int(number)
    else:
        numbers = driver.find_element(By.XPATH,
                                      '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[1]/a/em').text
        number = numbers.replace(',', '')
        cnt += int(number)
        #print(1, int(number))
        # cnt += int(driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[3]/a/em').text)
        numbers = driver.find_element(By.XPATH,
                                      '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a/em').text
        number = numbers.replace(',', '')
        cnt += int(number)
elif len(target) == 2:
    numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[1]/a/em').text
    number = numbers.replace(',', '')
    cnt += int(number)

    numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a/em').text
    number = numbers.replace(',', '')
    cnt += int(number)
elif len(target) == 1:
    # print(driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span/a/em').text)
    numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span/a/em').text
    number = numbers.replace(',', '')
    cnt += int(number)

print(cnt)
