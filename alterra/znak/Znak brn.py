import fake_user_agent
import requests
import requests.packages
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from pandas import DataFrame
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from urllib3.exceptions import InsecureRequestWarning


urllib3.disable_warnings(category=InsecureRequestWarning)
url = 'https://znakooo.ru/catalog/'


max_pg=[]
catalog_url = []
new_url = []
linkages = []
type=[]
prices = []
names = []
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'lxml')
btn = soup.find_all(class_="collection")

for group in btn:

    group_href = group.find("a").get("href").strip()
    x = url[:-9] + group_href
    print(x)
    response = requests.get(x, verify=False)

    soup = BeautifulSoup(response.text, 'lxml')
    mxpgs = soup.find("div",class_="products__list products__list_e1").get("data-showmore").split(",")
    max_page = mxpgs[0]
    print(max_page)
    for i in range(1, int(max_page)+1):
        link = url[:-9] + group_href + f"?PAGEN_4={i}"
        response = requests.get(link, verify=False)

        soup = BeautifulSoup(response.text, "lxml")
        old_pr = soup.find_all(class_="name p-product__title")
        for op in old_pr:

            hrf = op.find("a").get("href")

            last_link = url[:-9]+hrf
            response = requests.get(last_link, verify=False)

            soup = BeautifulSoup(response.text, 'lxml')
            cardprice = soup.find(class_="p-price p-price_strong").text.strip()
            types = soup.find(class_="p-price").text.strip()
            if "шт" in types:
                type.append("Цена ЗнакБарнаул за шт")
            elif "Уп" in types:
                type.append("Цена ЗнакБарнаул за Уп")
            elif "пог. м" in types:
                print("Return on the baseeeeeeeeeeeeeeeeee")
                type.append("Цена ЗнакБарнаул за пог. м")
            name = soup.find(class_="product-title").text
            linkages.append(last_link)
            names.append(name)
            prices.append(types[:-11])
print(type)
print(len(type))
print(len(names))
print(len(prices))
print(len(linkages))

new_slovar = {
    "Код": 1,
    "Конкуренты": "Знак Барнаул",
    "Артикул": "_",
    "Наименование": names,
    "Вид цены": type,
    "Цена": prices,
    "Ссылка": linkages

}
df = pd.DataFrame(new_slovar)
path = os.path.abspath("../Выгрузка цен Знак.xlsx")
if os.path.exists(path):
    flag = open(path, "r")
    flag.close()
    os.remove(path)
    path = os.path.abspath("../Выгрузка цен Знак.xlsx")
    df.to_excel("C:\\Users\\Admin\\PycharmProjects\\edu2023\\alterra\\Выгрузка цен Знак.xlsx", sheet_name="Лист 1", index=False)
else:
    with ExcelWriter(path, mode="w") as writer:
        df.to_excel(writer, sheet_name="Лист 1")






