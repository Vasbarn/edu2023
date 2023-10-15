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

def get_adres(url: str) -> list:
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, "lxml")
    adr = soup.find_all("div", class_="_13eh3hvq")
    print(adr)
def get_rating(url: str) -> list:
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, "lxml")
    contains = soup.find_all("div",class_="_y10azs")
    for cont in contains:
        print(cont)



path = os.path.abspath("Список магазинов.xlsx")
links: dict = get_links(path).get("Ссылка")
for link in links.values():
    # get_rating(link)
    get_adres(link)
    break