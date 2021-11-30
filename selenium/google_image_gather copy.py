# 키보드로 검색 키워드를 입력받는다.
# 현재 디렉토리에 검색 키워드의 폴더를 생성한다.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import create_dir_

search_name = input("검색하고 싶은 키워드: ")
search_limit = input("검색 갯수 입력: ")
search_url = "https://wwww.google.com/search?=" + str(search_name)
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get(search_url)
chrome.implicitly_wait(2)
image_count = len(chrome.find_elements_by_tag_name("img"))
print("로드된 이미지 개수 : ", image_count)

# 파일을 저장하기 위한 디렉토리 생성 함수 호출
search_path = os.path.dirname(os.path.realpath(__file__)) + "/"
create_dir_.search_selenium(search_name, search_path)
for i in range(search_limit) :
    image = chrome.find_elements_by_tag_name("img")[i]

    # search_path + search_name + str(i) + ".png"
    # 현재작업디렉토리dog0.png
    image.screenshot(search_path + search_name + str(i) + ".png")

chrome.close()