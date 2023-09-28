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

def get_rating(url: str) -> list:
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, "lxml")
    contains = soup.find(class_="_awwm2v")
    cont2 = contains.find_all("div")
    print(contains)



path = os.path.abspath("Список магазинов.xlsx")
links: dict = get_links(path).get("Ссылка")
for link in links.values():
    get_rating(link)
    break





