from selenium import webdriver
from selenium_stealth import stealth
import time

chrome = webdriver.Chrome()

stealth(chrome,
        languages=["ko-KR", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
chrome.get(url)

time.sleep(5)

chrome.quit()
