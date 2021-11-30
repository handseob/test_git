from selenium import webdriver
import time
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("http://naver.com")
time.sleep(3)
chrome.close()   #현재 tab만 종료
#chrome.quit()   #tab 모두 종료