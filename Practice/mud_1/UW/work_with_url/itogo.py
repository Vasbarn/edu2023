import requests
from bs4 import BeautifulSoup
import json
linkages = []
name_list = []
price_list = []
art_list = []
slovar = {}
pagination = 68
response = requests.get("https://formulam2.ru/catalog/02_lakokrasochnye_materialy/")
soup = BeautifulSoup(response.text, "lxml")
test = soup.find_all("div", class_="product-card__title")
for elem in test:
    link = elem.find('a')["href"]
    linkages.append(link)


for link in linkages:
    response = requests.get("https://formulam2.ru" + link)
    soup = BeautifulSoup(response.text, "lxml")
    name = soup.find(class_="product-card__title").text
    name = name.replace("\n","")
    print(name)
    name_list.append(name)
    print(name_list)
    price = soup.find(class_ = "product-info__content-main").text
    price_list.append(price)
    article = soup.find(class_="product-detail__code-number").text
    art_list.append(article)
for art, nam, cost in zip(art_list, name_list, price_list):
    slovar[art] = {"Наименование": nam, "Цена": cost}
print(slovar)

with open("Pars_complet.json", "w", encoding="utf-8") as file:
     file.write(json.dumps(slovar, ensure_ascii=False, indent=4))




