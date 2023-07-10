from operator import le
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome = webdriver.Chrome()
wait = WebDriverWait(chrome, 10)

category = {
    "cpu": "873",
    "메인보드": "875",
    "메모리": "874",
    "그래픽카드": "876",
    "ssd": "32617",
    "케이스": "879",
    "파워": "880"
}


def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))


def finds_present(css):
    find_present(css)
    return chrome.find_elements(By.CSS_SELECTOR, css)


def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))


def finds_visible(css):
    find_visible(css)
    return chrome.find_elements(By.CSS_SELECTOR, css)


def choose_one(text, options):
    print("-------------------------")
    print(text)
    print("-------------------------")

    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    choose = input("-> ")
    return int(choose) - 1


def parse_products():
    products = []
    try:
        finds_products = finds_visible(
            "table.tbl_list tr[class^=productList_]")

        for p in finds_products:
            try:
                name = p.find_element(By.CSS_SELECTOR, "p.subject a").text
                price = p.find_element(By.CSS_SELECTOR, "span.prod_price").text
            except:
                continue
            products.append((name, price))
    except:
        pass
    return products


def go_to_category(category_name):
    find_visible(category_css[category_name]).click()
    time.sleep(1)


def manufacturing_company(category):
    options_name = finds_visible(
        "div.search_option_list>div.search_option_item:first-child span.item_text")
    options = finds_visible(
        "div.search_option_list>div.search_option_item:first-child label.item_checkbox")
    i = choose_one(f"{category} 제조사를 골라주세요", [x.text for x in options_name])
    options[i].click()
    if category == "CPU":
        return i


def find_option_checkboxes(option_idx):
    return finds_visible(
        f"div.search_option_list>div.search_option_item:nth-child({option_idx}) label.item_checkbox")


def find_option_names(option_idx):
    return finds_visible(
        f"div.search_option_list>div.search_option_item:nth-child({option_idx}) span.item_text")


def more_btn_click(btn_idx):
    finds_visible("button.btn_item_more")[btn_idx].click()


def option_select(category_option, option_idx):
    option_names = find_option_names(option_idx)
    option_checkboxes = find_option_checkboxes(option_idx)
    i = choose_one(f"{category_option}(을/를) 골라주세요",
                   [x.text for x in option_names])
    option_checkboxes[i].click()


category_css = {
    c: "dd.category_" + category[c] + " a" for c in category
}


url = "http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti"
chrome.get(url)

# cpu 카테고리 클릭
go_to_category("cpu")

# cpu 제조사 불러오기
idx = manufacturing_company("CPU")
intel_or_amd = idx

# cpu 종류 불러오기
more_btn_click(idx)
options_name = find_option_names(idx + 2)
options = find_option_checkboxes(idx + 2)
i = choose_one("CPU 종류를 선택해 주세요.", [x.text for x in options_name])
options[i].click()
time.sleep(0.5)

# cpu 목록 선택
# table.tbl_list tr[class^=productList_] p.subject a 상품 이름
# table.tbl_list tr[class^=productList_] span.prod_price 상품 가격
cpus = parse_products()

# 메인보드
go_to_category("메인보드")

# 메인보드 제조사
more_btn_click(0)
manufacturing_company("메인보드")

# 메인보드 제품 분류
find_option_checkboxes(2)[intel_or_amd].click()
time.sleep(0.5)

# 소켓 부분은 선택 제외하고 메인보드 목록가져오기
mainboards = parse_products()

# 메모리
go_to_category("메모리")

# 메모리 제조사
more_btn_click(0)
manufacturing_company("메모리")

# 메모리 사용장치 데스크탑용
find_option_checkboxes(2)[0].click()

# 메모리 제품 분류 ddr5
find_option_checkboxes(3)[0].click()

# 메모리 용량 선택
more_btn_click(2)
option_select("메모리 용량", 4)
time.sleep(0.5)

# 메모리 목록 가져오기
memories = parse_products()

# 그래픽카드
go_to_category("그래픽카드")

# 제조사 선택
more_btn_click(0)
manufacturing_company("그래픽카드")

# 제조사 칩셋
find_option_checkboxes(2)[intel_or_amd].click()

if intel_or_amd == 0:
    category_option = "NVIDIA 칩셋"
else:
    category_option = "AMD 칩셋"
more_btn_click(intel_or_amd + 3)

option_select(category_option, intel_or_amd + 5)
time.sleep(0.5)

# 그래픽카드 목록 가져오기
graphics = parse_products()

# SSD
go_to_category("ssd")

# 제조사 선택
more_btn_click(0)
manufacturing_company("SSD")

# 용량 선택
more_btn_click(4)
option_select("용량", 5)
time.sleep(0.5)

# ssd 목록 가져오기
ssds = parse_products()

# 케이스
go_to_category("케이스")

# 제조사 선택
more_btn_click(0)
manufacturing_company("케이스")

# 제품 분류
# more_btn_click(1)
# option_select("제품 분류", 2)

# 케이스 크기
more_btn_click(2)
option_select("케이스 크기", 3)
time.sleep(0.5)

# 케이스 목록 가져오기
cases = parse_products()

# 파워
go_to_category("파워")

# 제조사 선택
more_btn_click(0)
manufacturing_company("파워")

# 정격출력
more_btn_click(2)
option_select("정격출력", 3)

# 80PLUS인증
more_btn_click(3)
option_select("80PLUS인증", 4)
time.sleep(0.5)

# 파워 목록 가져오기
powers = parse_products()

# cpus, mainboards, memories, graphics, ssds, cases, powers


def product_check(arr):
    if len(arr) == 0:
        return ["물품이 존재하지 않습니다."]
    return arr


popular = {
    "cpu": product_check(cpus)[0],
    "mainboard": product_check(mainboards)[0],
    "memory": product_check(memories)[0],
    "graphic": product_check(graphics[0]),
    "ssd": product_check(ssds[0]),
    "case": product_check(cases[0]),
    "power": product_check(powers)[0]
}

print()

# 인기 조합
print("인기 1위 조합 입니다.")
print("cpu")
print(popular["cpu"])

print("mainboard")
print(popular["mainboard"])

print("memory")
print(popular["memory"])

print("ssd")
print(popular["ssd"])

print("case")
print(popular["case"])

print("power")
print(popular["power"])

# 가성비
cpu = min([x[1] for x in cpus])


def find_cheap(arr):
    if len(arr) == 0:
        return "물품이 존재하지 않습니다."

    cheap_idx = 0
    for i in range(len(arr)):
        cheap = arr[cheap_idx]
        product = arr[i]
        if int(product[1].replace(',', '')) < int(cheap[1].replace(',', '')):
            cheap_idx = i
    return arr[cheap_idx]


print()
print("----------------------------------------")
print()

recommend = {
    "cpu": find_cheap(cpus),
    "mainboard": find_cheap(mainboards),
    "memory": find_cheap(memories),
    "graphic": find_cheap(graphics),
    "ssd": find_cheap(ssds),
    "case": find_cheap(cases),
    "power": find_cheap(powers)
}

print("가성비 조합 입니다.")
print("cpu")
print(recommend["cpu"])

print("mainboard")
print(recommend["mainboard"])

print("memory")
print(recommend["memory"])

print("ssd")
print(recommend["ssd"])

print("case")
print(recommend["case"])

print("power")
print(recommend["power"])

chrome.quit()
