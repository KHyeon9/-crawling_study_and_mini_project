from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.headless = True

chrome = webdriver.Chrome(options)
wait = WebDriverWait(chrome, 10)


def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))


def finds_visible(css):
    find_visible(css)
    return chrome.find_elements(By.CSS_SELECTOR, css)


chrome.get("https://www.naver.com/")

find_visible("input#query").send_keys("패스트캠퍼스\n")
finds_visible("a[role=tab]")[1].click()

e = find_visible("li[data-cr-rank='6']")

#  특정 엘리먼트만 스크린 샷
# e.screenshot("./test.png")

# 특정 부분에 css 스타일 넣기
chrome.execute_script(
    """
    document.querySelector("li[data-cr-rank='6']").setAttribute('style', 'border:10px solid red')
    """)

# 전체 화면 스크린샷
# chrome.save_screenshot("./test.png")
chrome.set_window_size(1000, 10000)
body = find_visible("body")
body.screenshot("./test.png")


chrome.quit()
