import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://dir.indiamart.com/lucknow/oxygen-cylinders.html')
# print(r.text)

beauti = bs(r.text, "html.parser")
# print(beauti.prettify())

info_div = beauti.find_all('div', attrs={'class': 'r-cl'})


for info in info_div:
    name = info.find_all('h4', attrs={'class': 'lcname'})
    phone = info.find_all('span', attrs={'class': 'pns_h'})
    list = []
    for n in name:
        print(n.get_text())
    for p in phone:
        print(p.get_text())


