from selenium import webdriver
URL = 'http://localhost:4444/wd/hub'

browser = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    options=webdriver.ChromeOptions()
)
browser.get("http://naver.com")
print(browser.title)
browser.close()
