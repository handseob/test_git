from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support
from webdriver_manager.chrome import ChromeDriverManager 
import time

for i in range(8):
    chrome.execute_script("window.scrollBy(0, " + str((i+1) * 1000) + ")")
    time.sleep(1)  #loading 할때까지 좀 기다려줌

# # div 태그의 class의 속성 값이 basicList_link__로 시작하는 것 가져오기
items = short_wait.until(EC.visibility_of_all_elements_located((
    By.CSS_SELECTOR, "div[class ^= basicList_info_area__")))

for item in items :
    # 광고 걸러내기
    try:
        item.find_element_by_css_selector("button[class ^= ad_")
        continue
    except:
        pass
    print(item.find_element_by_css_selector("a[class ^= basicList_link__]").text)