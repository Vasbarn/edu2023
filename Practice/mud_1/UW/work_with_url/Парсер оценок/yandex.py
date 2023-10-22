import requests
from bs4 import BeautifulSoup
import json
from typing import Dict
import pandas
import os

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                            "Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36"}
def get_links(way: str) -> Dict[str, str]:
    df = pandas.read_excel(way, index_col="Название магазина")
    return df.to_dict()


def get_rating(url: str, adres: str, listing: list) -> list:
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, "lxml")
    main = soup.find(class_ = "business-header-rating-view__user-rating")

    rate = main.find(class_ = "business-rating-badge-view__rating-text _size_m")
    calls = main.find(class_ = "business-header-rating-view__text _clickable")
    print(rate)
    print(calls)
    diction = {}
    diction["Количество отзывов"] = calls.text
    diction["Рейтинг"] = rate.text
    diction["Название магазина"] = adres
    listing.append(diction)





spisok = []
path = os.path.abspath("Магазины Яндекс.xlsx")
links: dict = get_links(path).get("Ссылка")
for key,value in links.items():
    get_rating(value,path,spisok)

# dataf = pandas.DataFrame(spisok)
# otkritie = pandas.read_excel(path, sheet_name = "Лист1")
# df = otkritie.merge(dataf, left_on="Название магазина", right_on="Название магазина")
# df.to_excel(path, sheet_name= "Лист2", index=False)
# print(df)