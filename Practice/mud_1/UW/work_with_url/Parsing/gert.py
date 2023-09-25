import requests
from bs4 import BeautifulSoup
import json
from typing import Dict
# slovar = {}
# pagination = 5
# response = requests.get("https://formulam2.ru/catalog/02_lakokrasochnye_materialy/")
# soup = BeautifulSoup(response.text, "lxml")
# max_page = int(soup.find_all(class_="pagination__link")[-1].text.strip())
# for nump in range(1, max_page+1):
#     response = requests.get(f"https://formulam2.ru/catalog/02_lakokrasochnye_materialy/?PAGEN_1={nump}")
#     soup = BeautifulSoup(response.text, "lxml")
#     goods = soup.find_all("div", class_="product-card products-grid__item")
#     for good in goods:
#         link = "https://formulam2.ru" + good.find(class_="product-card__title").find("a").get("href")
#         name = good.find(class_="product-card__title").text.strip()
#         article = good.find(class_="product-card__index").text.replace("Код:", '').strip()
#         price = float(good.find(class_ = "product-card__new-price").find("span").text.replace(' ', '').strip())
#         slovar[article] = dict(Наименование=name, Цена=price, Ссылка=link)
#     print(nump)
#     print(str(nump) + "/" + str(max_page), end="\r")
#
# with open("Pars_complet.json", "w", encoding="utf-8") as file:
#     file.write(json.dumps(slovar, ensure_ascii=False, indent=4))