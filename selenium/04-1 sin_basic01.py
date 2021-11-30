# chromedriver의 다양한 옵션 살펴보기
# chromedriver static하게 경로지정하기(절대경로)
# chrome 브라우저 제어하기

from selenium import webdriver
import time                     # 셀레니움 실행시 기다려야하는 시간들이 있음.

#크롬 옵션 주기, 크롬을 실행시킬때 함수를 실행하듯이 할 수 있음.
options = webdriver.ChromeOptions()               #옵션 설정 객체생성
options.add_argument("window-size=1000,1000")     # 실행 윈도우 크기
options.add_argument("no-sandbox")                # 샌드박스 사용 안하겠다. 텝별로 분리하겠다. 거리를 두겠다
# options.add_argument("headless")                # 크롬창을 안뜨게함


driver_path = '/home/handseob/datagather/selenium/chromedriver'
chrome = webdriver.Chrome(driver_path, options=options)
chrome.get("http://naver.com")                    # 브라우저로 url 실행
chrome.get("http://shopping.naver.com")
chrome.back
time.sleep(2)
chrome.forward()
time.sleep(2)
# chrome.close()                                   #현재 tab만 종료

