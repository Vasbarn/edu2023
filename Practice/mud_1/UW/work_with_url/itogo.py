import requests
from bs4 import BeautifulSoup
import json
from typing import Dict


def get_requisits(borsch: "BeautifulSoup", diction: Dict[str, dict]) -> None:
    """Получаем основные реквизиты позиций и добавляем их в словарь"""
    link = "https://formulam2.ru" + borsch.find(class_="product-card__title").find("a").get("href")
    name = borsch.find(class_="product-card__title").text.strip()
    article = borsch.find(class_="product-card__index").text.replace("Код:", '').strip()
    price = float(borsch.find(class_="product-card__new-price").find("span").text.replace(' ', '').strip())
    diction[article] = dict(Наименование=name, Цена=price, Ссылка=link)

def get_max_page(url: str) -> int:
    """Получаем максимальное количество страниц в каталоге"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    max_page = int(soup.find_all(class_="pagination__link")[-1].text.strip())
    return max_page


# slovar = {}
# pagination = 5
# response = requests.get("https://formulam2.ru/catalog/02_lakokrasochnye_materialy/")
# soup = BeautifulSoup(response.text, "lxml")
# max_page = int(soup.find_all(class_="pagination__link")[-1].text.strip())
# for nump in range(1, 4+1):
#     response = requests.get(f"https://formulam2.ru/catalog/02_lakokrasochnye_materialy/?PAGEN_1={nump}")
#     soup = BeautifulSoup(response.text, "lxml")
#     goods = soup.find_all("div", class_="product-card products-grid__item")
#     for good in goods:
#         get_requisits(good, slovar)
#     print(nump)
#     print(str(nump) + "/" + str(max_page), end="\r")

page = get_max_page("https://formulam2.ru/catalog/01_sukhie_smesi_teploizolyatsiya_gipsokarton/gipsokarton_gipsovolokno_lenty_setki/gkl_gvl/")
print(page)
# with open("Pars_complet.json", "w", encoding="utf-8") as file:
#     file.write(json.dumps(slovar, ensure_ascii=False, indent=4))






