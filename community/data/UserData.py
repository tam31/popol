from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #selenium에서 사용할 모듈 import
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



def userdata(name):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://map.naver.com/v5/search/" + name) #네이버 지도에 여행지명 검색
    try:
       element = WebDriverWait(driver, 20).until(
           EC.presence_of_element_located((By.CSS_SELECTOR,"iframe#searchIframe"))
       ) #입력창이 뜰 때까지 대기
    finally:
       pass

    time.sleep(4) #화면 표시 기다리기
    frame = driver.find_element(By.CSS_SELECTOR,"iframe#searchIframe") # 프레임 지정하기
    driver.switch_to.frame(frame)
    time.sleep(1)

    #해당여행지가 없을때 방문자 수 0
    Box = driver.find_elements(By.XPATH, '//*[@id="app-root"]/div/div[2]/div')
    if len(Box) == 1:
        return 0

    firstBox = driver.find_elements(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li')
    Box = driver.find_elements(By.XPATH, '//*[@id="app-root"]/div/div[1]/div')

    if len(Box) == 1:
        driver.find_element(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/a/div/div').click() #food용
        #driver.find_element(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li/div[1]/div/a/div[1]/div').click() Tour용

    else:
        if len(firstBox) > 1:
            check = driver.find_elements(By.XPATH,'//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div')
            
            if len(check) >= 3:  # 사진이 있고 없고로 갯수가 나눠서 바뀜
                driver.find_element(By.XPATH,
                                    '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/div[2]/a[1]/div/div').click()
            else:
                driver.find_element(By.XPATH,
                                    '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/div[2]/a[1]/div/div').click()


    #프레임 지정 지우기(새로 생긴프레임을위해)
    driver.switch_to.default_content()
    time.sleep(4)
    #새로 생긴 프레임지정
    driver.switch_to.frame(driver.find_element(By.ID, 'entryIframe'))
    time.sleep(4)

    cnt = 0 #총 방문자수
    target = driver.find_elements(By.XPATH,'//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span')
    if len(target) >= 3: #리뷰의 수가 3, 2개, 1개로 나뉨
        if driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a').text.split()[0] == '방문자리뷰':

            numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a/em').text
            number=numbers.replace(',','')
            cnt += int(number)

            numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[3]/a/em').text
            number = numbers.replace(',', '')
            cnt += int(number)
        else:
            numbers = driver.find_element(By.XPATH,
                                          '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[1]/a/em').text
            number = numbers.replace(',', '')
            cnt += int(number)

            numbers = driver.find_element(By.XPATH,
                                          '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a/em').text
            number = numbers.replace(',', '')
            cnt += int(number)
    elif len(target) == 2:
        numbers = driver.find_element(By.XPATH,'//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[1]/a/em').text
        number = numbers.replace(',', '')
        cnt += int(number)

        numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a/em').text
        number = numbers.replace(',', '')
        cnt += int(number)
    elif len(target) == 1:
        numbers = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span/a/em').text
        number = numbers.replace(',', '')
        cnt += int(number)
    return cnt

