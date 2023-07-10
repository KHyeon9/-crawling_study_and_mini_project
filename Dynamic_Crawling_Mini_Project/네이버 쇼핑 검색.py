from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

chrom = webdriver.Chrome(options=options)
chrom.get("https://shopping.naver.com")

# 로딩을 기다리는 방법
# 1. time.sleep(3) 파이썬이 멈춤
# 2. chrom.implicitly_wait(3) seleninum chrome driver가 멈춤
# 1, 2번은 모든 페이지에서 적용이 안될 수 있다.
# 3. WebDriverWait(chrom, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[class^=_searchInput_search_text]")))
# 로딩이 되길 원하는 element를 지정하여 로딩 될때 까지 멈출 수 있다 또한 해당 element를 찾지 못한다면 기다리는 시간을 지정할 수 있다.

wait = WebDriverWait(chrom, 10)
# el = wait.until(EC.presence_of_element_located(
#     (By.CSS_SELECTOR, "input[class^=_searchInput_search_text]")))


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


search = find(wait, "input[class^=_searchInput_search_text]")
search.send_keys("아이폰 케이스\n")

time.sleep(3)

# button = find(
#     wait, "div[class^=_searchInput_search_input_]>button:last-child")
# button.click()

# time.sleep(3)

chrom.close()
