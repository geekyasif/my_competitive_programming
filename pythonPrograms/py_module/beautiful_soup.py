import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/country/us/"
html = requests.get(url)
# print(html.content)

bs4Soup = BeautifulSoup(html.text, "html.parser")
# print(bs4Soup.prettify())


info_dict = {}


info_div = bs4Soup.find('div', attrs={'class':'content-inner'})
# print(info_div)

for info in info_div.find_all('div',attrs={'id':'maincounter-wrap'}):
    try:
        heading = info.h1.get_text()
        count = info.span.get_text()
        print(heading)
        print(count)
    except AttributeError:
        print('')
    # info_dict[heading] = count


print('''Coronavirus Cases in India\n''')
# for i,j in info_dict.items():
#     print(i,j)

