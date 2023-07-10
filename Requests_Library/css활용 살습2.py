from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
accept_language = "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
hdr = {'User-Agent': user_agent,
       'Accept-Language': accept_language}

res = req.get(url, headers=hdr)
soup = BS(res.text, "html.parser")

for desc in soup.select("div.descriptions-inner"):
    ads = desc.select("span.ad-badge")

    if len(ads) > 0:
        print("광고!")
    print(desc.select("div.name")[0].get_text(strip=True))
