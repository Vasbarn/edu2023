import requests
from bs4 import BeautifulSoup
import json
from typing import Dict
import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from openpyxl import *


url = "https://barnaul.tstn.ru/shop/"
response = requests.get(url)
print(response)
# blink = "https://barnaul.tstn.ru/" + borsch.find(class_="catalog-item__name").find("a").get("href")
# name = borsch.find(class_="product-card__title").text.strip()
# article = borsch.find(class_="product-card__index").text.replace("Код:", '').strip()
# price = float(borsch.find(class_="product-card__new-price").find("span").text.replace(' ', '').strip())
# quantity = borsch.find("div", class_="product-card__new-price").text.split("/")[1]
# diction[article] = dict(Наименование=name, Цена=price, Ссылка=blink,
#                         Единица_измерения="Цена ФормулаМ2Горный за" + quantity, Конкуренты="ФормулаМ2Горный")
