from bs4 import BeautifulSoup as BS
import requests as req

url = "https://finance.yahoo.com/most-active"
res = req.get(url)
soup = BS(res.text, "html.parser")

for tr in soup.select("table tbody tr"):
    title = tr.select("td:nth-child(1) a")[0].get_text(strip=True)
    price = tr.select("td:nth-child(3) fin-streamer")[0].get_text(strip=True)
    change = tr.select("td:nth-child(5) span")[0].get_text(strip=True)
    print(title, price, change)
