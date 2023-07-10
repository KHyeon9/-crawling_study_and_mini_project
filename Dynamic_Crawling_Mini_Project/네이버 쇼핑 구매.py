from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip


def vis_find_css_selector(wait, css_selector):
    return wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, css_selector)))


def pre_find_css_selector(wait, css_selector):
    return wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, css_selector)))


chrome = webdriver.Chrome()
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com")
# wait.until(EC.visibility_of_element_located(
#     (By.CSS_SELECTOR, "a#gnb_login_button"))).click()
vis_find_css_selector(wait, "a#gnb_login_button").click()

input_id = vis_find_css_selector(wait, "input#id")
input_pw = vis_find_css_selector(wait, "input#pw")
login_btn = vis_find_css_selector(wait, "button.btn_login")

# pip install pyperclip
pyperclip.copy("아이디가 들어가는 부분")
# input_id.send_keys(Keys.COMMAND, "v")  mac
input_id.send_keys(Keys.CONTROL, "v")  # window

pyperclip.copy("비밀번호가 들어가는 부분")
input_pw.send_keys(Keys.CONTROL, "v")

login_btn.click()

pre_find_css_selector(short_wait, "a#gnb_logout_button")

search = vis_find_css_selector(wait, "input[class^=_searchInput_search_text_]")
search.send_keys("아이폰 케이스")
time.sleep(1)
search.send_keys("\n")

# 스크롤
# for i in range(8):
#     chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)")
#     time.sleep(1)

# vis_find_css_selector(wait, "a[class^=product_link__]")

# 광고 빼기(예전이랑 바뀌어서  클래스가 다르기 때문에 상관없지만 실습 원에 해봄)
# products = chrome.find_elements(By.CSS_SELECTOR, "div[class*=roduct_info_]")
# for product in products:
#     try:
#         ad = product.find_element(By.CSS_SELECTOR, "button[class^=ad_ad_]")
#         print(ad.text)
#         continue
#     except:
#         pass
#     title = product.find_element(By.CSS_SELECTOR, "a[class*=roduct_link__]")
#     print(title.text)

# titles = chrome.find_elements(By.CSS_SELECTOR, "a[class^=product_link__]")
# for title in titles:
#     print(title.text)

vis_find_css_selector(wait, "a[class^=product_link__]").click()

time.sleep(2)

switch_tab = chrome.window_handles[1]

chrome.switch_to.window(switch_tab)

# 상품 상세페이지
# 옵션 고른뒤에
# 구매 버튼

vis_find_css_selector(wait, "a[aria-haspopup='listbox']")
options = chrome.find_elements(By.CSS_SELECTOR, "a[aria-haspopup='listbox']")

options[0].click()
time.sleep(0.1)
chrome.find_element(
    By.CSS_SELECTOR, "ul[role=listbox] li:nth-child(2) a[role=option]").click()

options[1].click()
time.sleep(0.1)
chrome.find_element(
    By.CSS_SELECTOR, "ul[role=listbox] li:nth-child(6) a[role=option]").click()

# 결제하기 버튼
chrome.find_element(By.CSS_SELECTOR, "div[class*='N=a:pcs.buy']>a").click()

vis_find_css_selector(wait, "button[class*=_doPayButton]").click()

time.sleep(5)

# 다음 결제 번호 입력은 실제로 결제 되기 때문에 제외

chrome.quit()
