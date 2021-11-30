from selenium import webdriver
import time
# selenium webdriver는 크롬 브라우저 버전 전용을 사용해야함.
# 실습path : /home/자신homeid/datagather/selenium/chrome

from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver_path = "/home/handseob/datagather/selenium/chrome"
chrome.get("http://naver.com")
time.sleep(3) #단위 : sec
chrome.close()