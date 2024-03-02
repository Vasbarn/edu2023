import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(category=InsecureRequestWarning)
from multiprocessing import Pool
from threading import Thread
import sys
import time
potoks = []
names = []
types = []
linkages =[]
prices = []
cardprices = []
names_ga= []
types_ga= []
linkages_ga =[]
prices_ga = []
cardprices_ga= []
articles = []
hrefs = []
pages = []
items = []
items_ga = []
articles_ga = []
sys.setrecursionlimit(10000)
datas={}
def get_page_data_brn(href, page):

    # link = "https://znakooo.ru" + href + f"?PAGEN_4={page}"
    link = "https://znakooo.ru/catalog/dveri/" + f"?PAGEN_4={page}"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "lxml")
    old_pr = soup.find_all(class_="name p-product__title")
    for op in old_pr:
        hrf = op.find("a").get("href")
        last_link = "https://znakooo.ru" + hrf
        linkages.append(last_link)
        try:
            response = requests.get(last_link)
            soup = BeautifulSoup(response.text, 'lxml')

        except(requests.exceptions.ConnectTimeout,AttributeError, PermissionError):
            print("r", end="")
            continue
        name = soup.find(class_="product-title").text
        names.append(name)
        cardprice = soup.find(class_="p-price p-price_strong").text.strip()
        cardprices.append(cardprice)
        type = soup.find(class_="p-price").text.strip()
        price = type.split("руб.")[0]
        prices.append(price)
        if "шт" in type:
            types.append("Цена ЗнакБарнаул за шт")
        elif "Уп" in type:
            types.append("Цена ЗнакБарнаул за Уп")
        elif "пог. м" in type:
            types.append("Цена ЗнакБарнаул за пог. м")
        article = soup.find_all(class_="product-characteristics")
        for art in article:
            a = art.find_all("span")
            artings = a[-1:]
            for val in artings:
                articles.append(val.text)










# def get_page_data_ga(href, page):
#     start = time.time()
#     link = "https://galtaysk.znakooo.ru"+ href + f"?PAGEN_4={page}"
#     response = requests.get(link)
#     soup = BeautifulSoup(response.text, "lxml")
#     old_pr = soup.find_all(class_="name p-product__title")
#     for op in old_pr:
#         hrf = op.find("a").get("href")
#         last_link = "https://galtaysk.znakooo.ru" + hrf
#         try:
#             response = requests.get(last_link)
#             soup = BeautifulSoup(response.text, 'lxml')
#         except(requests.exceptions.ConnectTimeout):
#             print("r", end="")
#             continue
#         name = soup.find(class_="product-title").text
#         cardprice = soup.find(class_="p-price p-price_strong").text.strip()
#         type = soup.find(class_="p-price").text.strip()
#         price = type.split("руб.")[0]
#         if "шт" in type:
#             types_ga.append("Цена ЗнакМайма за шт")
#         elif "Уп" in type:
#             types_ga.append("Цена ЗнакМайма за Уп")
#         elif "пог. м" in type:
#             types_ga.append("Цена ЗнакМайма за пог. м")
#         article = soup.find_all(class_="product-characteristics")
#         for art in article:
#             a = art.find_all("span")
#             artings = a[-1:]
#             for val in artings:
#                 articles_ga.append(val.text)
#             names_ga.append(name)
#             cardprices_ga.append(cardprice)
#             linkages_ga.append(last_link)
#             prices_ga.append(price)
#     end = time.time()


def gather_data_brn():

    url = 'http://znakooo.ru/catalog/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    btn = soup.find_all(class_="collection")
    for group in btn:

        group_href = group.find("a").get("href").strip()

        x = url[:-9] + group_href
        respon = requests.get(x)
        soup = BeautifulSoup(respon.text, 'lxml')

        mxpgs = soup.find("div", class_="products__list products__list_e1").get("data-showmore").split(",")

        max_page = mxpgs[0]
        for i in range(1, int(max_page) + 1):
            items.append((group_href, i))





def gather_data_ga():
    url = 'http://galtaysk.znakooo.ru/catalog/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    btn = soup.find_all(class_="collection")
    for group in btn:

        group_href = group.find("a").get("href").strip()

        x = url[:-9] + group_href
        respon = requests.get(x)
        soup = BeautifulSoup(respon.text, 'lxml')

        mxpgs = soup.find("div", class_="products__list products__list_e1").get("data-showmore").split(",")

        max_page = mxpgs[0]
        for i in range(1, int(max_page) + 1):
            items_ga.append((group_href, i))


def main(x):
    start = time.time()
    print(x)


    new_slovar = {
        "Код": 1,
        "Конкуренты": "Знак Барнаул",
        "Артикул": x[2],
        "Наименование": x[1],
        "Вид цены": x[5],
        "Цена": x[3],
        "Цена по карте": x[4],
        "Ссылка": x[0]
    }
    # new_slovar_ga = {
    #     "Код": 1,
    #     "Конкуренты": "Знак Майма",
    #     "Артикул": articles_ga,
    #     "Наименование": names_ga,
    #     "Вид цены": types_ga,
    #     "Цена": prices_ga,
    #     "Ссылка": linkages_ga
    # }

    df = pd.DataFrame(new_slovar)
    # df2 = pd.DataFrame(new_slovar_ga)
    path = os.path.abspath("../Выгрузка цен Знак1.xlsx")
    if os.path.exists(path):
        flag = open(path, "r")
        flag.close()
        os.remove(path)
        path = os.path.abspath("../Выгрузка цен Знак1.xlsx")
        writer = pd.ExcelWriter("Выгрузка цен Знак1.xlsx", engine="xlsxwriter")
        df.to_excel(writer,
                    sheet_name="Барнаул",
                    index=False)
        # df2.to_excel(writer,
        #             sheet_name="Майма",
        #             index=False)
    else:
        with ExcelWriter(path, mode="w") as writer:
            df.to_excel(writer, sheet_name="Барнаул")
            # df2.to_excel(writer, sheet_name="Майма")
    path = os.path.abspath("../Выгрузка цен Знак1.xlsx")
    end = time.time()
    print(end - start)


if __name__ == "__main__":

    gather_data_brn()
    pool = Pool(processes=60)
    datalist = pool.starmap(get_page_data_brn,items)
    # pool.starmap(get_page_data_ga,items_ga)
    main(datalist)


