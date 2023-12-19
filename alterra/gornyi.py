from bs4 import BeautifulSoup
import requests
import lxml

ssylki = []
links = []
path = []
names = []
articles = []
prices=[]
numb=[]
url = "https://gorniy.formulam2.ru/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
otdels = soup.find_all(class_="catalog__list-item depth_level_1")
for elem in otdels:
    href = elem.find_all("a")
    for i in href:
        thing = i.get("href")
        ssylki.append(thing)
x = ssylki[1]
url2 = url + x

response2 = requests.get(url2)
schi = BeautifulSoup(response2.text, "lxml")
way = schi.find_all(class_="product-card__title")
art = schi.find_all(class_ = "product-card__index")
price = schi.find_all(class_="product-card__new-price")
for el in way:
    fullway = el.find("a").get("href")
    name = el.find("div", class_ = "js-toclamp-4").text
    names.append(name)
    path.append(url+fullway)
for a in art:
    articles.append(a.text[4:])
for pr in price:
    g = pr.text.split("/")
    prices.append(g[0][:-2])
    numb.append("Цена ФормулаМ2Горный за" + g[1])
print(prices)
print(numb)



# for j in list(set(ssylki)):
#     url2 = url + j
#     # links.append(url2)
#     response2 = requests.get(url2)
#     soup = BeautifulSoup(response2.text, "lxml")
#     print(soup)

