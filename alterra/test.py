import requests
from bs4 import BeautifulSoup
import json
from typing import Dict
import pandas as pd

names = []


def get_requisits(borsch: "BeautifulSoup", diction: Dict[str, dict], listing: list) -> None:
    """Получаем основные реквизиты позиций и добавляем их в словарь"""
    blink = "https://gorniy.formulam2.ru/" + borsch.find(class_="product-card__title").find("a").get("href")
    name = borsch.find(class_="product-card__title").text.strip()
    listing.append(name)
    article = borsch.find(class_="product-card__index").text.replace("Код:", '').strip()
    price = float(borsch.find(class_="product-card__new-price").find("span").text.replace(' ', '').strip())
    quantity = borsch.find("div", class_="product-card__new-price").text.split("/")[1]
    diction[article] = dict(Наименование=name, Цена=price, Ссылка=blink,
                            Единица_измерения="Цена ФормулаМ2Горный за" + quantity)


def get_max_page(url: str) -> int:
    """Получаем максимальное количество страниц в каталоге"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    try:
        max_page = int(soup.find_all(class_="pagination__link")[-1].text.strip())
    except (IndexError, TypeError):
        max_page = 1
    return max_page


slovar = {}
response = requests.get("https://gorniy.formulam2.ru/catalog/")
soup = BeautifulSoup(response.text, "lxml")
links = soup.find_all("div", class_="catalog-sections-item__img")
for lin in links[0:5]:
    link = "https://gorniy.formulam2.ru/" + lin.find("a")["href"]

    page = get_max_page(link)
    for nump in range(1, 2):
        response = requests.get(f"{link}?PAGEN_1={nump}")
        soup = BeautifulSoup(response.text, "lxml")
        goods = soup.find_all("div", class_="product-card products-grid__item")
        for good in goods:
            get_requisits(good, slovar, names)

    with open("fkn.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(slovar, ensure_ascii=False, indent=4))

df = pd.DataFrame(slovar).transpose()
print(df)


# for j in list(set(ssylki)):
#     url2 = url + j
#     # links.append(url2)
#     response2 = requests.get(url2)
#     soup = BeautifulSoup(response2.text, "lxml")
#     print(soup)

