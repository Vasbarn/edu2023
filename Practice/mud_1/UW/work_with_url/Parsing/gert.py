import requests
from bs4 import BeautifulSoup
import json
from typing import Dict

def get_requisits(borsch: "BeautifulSoup", diction: Dict[str, dict]) -> None:
    """Получаем основные реквизиты позиций и добавляем их в словарь"""
    blink = "https://formulam2.ru" + borsch.find(class_="product-card__title").find("a").get("href")
    name = borsch.find(class_="product-card__title").text.strip()
    article = borsch.find(class_="product-card__index").text.replace("Код:", '').strip()
    price = float(borsch.find(class_="product-card__new-price").find("span").text.replace(' ', '').strip())
    diction[article] = dict(Наименование=name, Цена=price, Ссылка=blink)


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
response = requests.get("https://formulam2.ru/catalog/")
soup = BeautifulSoup(response.text, "lxml")
# imya = soup.find_all("div", class_="js-toclamp-2")
# for nam in imya:
#     naim_cat = nam.find("js-toclamp-2")[]
#     print(naim_cat)
links = soup.find_all("div", class_="catalog-sections-item__img")
for lin in links[0:5]:
    link = "https://formulam2.ru"+lin.find("a")["href"]

    page = get_max_page(link)
    for nump in range(1, 2):
        response = requests.get(f"{link}?PAGEN_1={nump}")
        soup = BeautifulSoup(response.text, "lxml")
        goods = soup.find_all("div", class_="product-card products-grid__item")
        for good in goods:

            get_requisits(good, slovar)


        print(nump)
        print(str(nump) + "/" + str(page), end="\r")

    with open("Final_pars.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(slovar, ensure_ascii=False, indent=4))