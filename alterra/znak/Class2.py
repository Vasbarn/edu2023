import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(category=InsecureRequestWarning)
from multiprocessing import Pool
import sys
import time
import itertools
sys.setrecursionlimit(10000)


class Znak():
    def __init__(self):
       self.datas = dict()
       self.articles = list()
       self.types = list()
       self.types_ga = []
       self.items = []
       self.items_ga = []
       self.datas_ga = []
    def get_page_data_brn(self, href, page):
        data = self.datas
        start = time.time()
        link = "https://znakooo.ru" + href + f"?PAGEN_4={page}"
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "lxml")
        old_pr = soup.find_all(class_="name p-product__title")
        for op in old_pr:
            hrf = op.find("a").get("href")
            last_link = "https://znakooo.ru" + hrf

            try:
                response = requests.get(last_link)
                soup = BeautifulSoup(response.text, 'lxml')
                name = soup.find(class_="product-title").text
            except(requests.exceptions.ConnectTimeout, AttributeError, PermissionError):
                print("r", end="")
                continue

            cardprice = soup.find(class_="p-price p-price_strong").text.strip()

            type = soup.find(class_="p-price").text.strip()
            price = type.split("руб.")[0]

            if "шт" in type:
                self.types.append("Цена ЗнакБарнаул за шт")
            elif "Уп" in type:
                self.types.append("Цена ЗнакБарнаул за Уп")
            elif "пог. м" in type:
                self.types.append("Цена ЗнакБарнаул за пог. м")
            article = soup.find_all(class_="product-characteristics")
            for art in article:
                a = art.find_all("span")
                artings = a[-1:]
                #     self.articles.append(val.text)
                for val,typing in itertools.product(artings, self.types):
                    data[val.text] = (last_link,name,price,cardprice,typing)
        print(data)
        return data



    def get_page_data_ga(self, href, page):
        data_ga = self.datas_ga
        start = time.time()
        link = "http://galtaysk.znakooo.ru" + href + f"?PAGEN_4={page}"
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "lxml")
        old_pr = soup.find_all(class_="name p-product__title")
        for op in old_pr:
            hrf = op.find("a").get("href")
            last_link = "https://znakooo.ru" + hrf

            try:
                response = requests.get(last_link)
                soup = BeautifulSoup(response.text, 'lxml')
                name = soup.find(class_="product-title").text
            except(requests.exceptions.ConnectTimeout, AttributeError, PermissionError):
                print("r", end="")
                continue

            cardprice = soup.find(class_="p-price p-price_strong").text.strip()

            type = soup.find(class_="p-price").text.strip()
            price = type.split("руб.")[0]

            if "шт" in type:
                self.types_ga.append("Цена ЗнакБарнаул за шт")
            elif "Уп" in type:
                self.types_ga.append("Цена ЗнакБарнаул за Уп")
            elif "пог. м" in type:
                self.types_ga.append("Цена ЗнакБарнаул за пог. м")
            article = soup.find_all(class_="product-characteristics")
            for art in article:
                a = art.find_all("span")
                artings = a[-1:]
                #     self.articles.append(val.text)
                for val,typing in itertools.product(artings, self.types_ga):
                    data_ga[val.text] = (last_link,name,price,cardprice,typing)

        return data_ga


    def gather_data_brn(self):
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
                self.items.append((group_href, i))

    def gather_data_ga(self):
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
                self.items_ga.append((group_href, i))
    #

    def main(self, x, y):
        keys = []
        names = []
        price = []
        cprice = []
        link = []
        type = []
        keys_ga = []
        names_ga = []
        price_ga = []
        cprice_ga = []
        link_ga = []
        type_ga = []
        for data_brn in x:
            for key, item in data_brn.items():
                keys.append(key)
                names.append(item[1])
                price.append(item[2])
                cprice.append(item[3])
                link.append(item[0])
                type.append(item[4])
        for data_ga in y:
            for key, item in data_ga.items():
                keys_ga.append(key)
                names_ga.append(item[1])
                price_ga.append(item[2])
                cprice_ga.append(item[3])
                link_ga.append(item[0])
                type_ga.append(item[4])


        new_slovar = {
            "Код": 1,
            "Конкуренты": "Знак Майма",
            "Артикул": keys,
            "Наименование": names,
            "Вид цены": type,
            "Цена": price,
            "Цена по карте": cprice,
            "Ссылка": link
        }
        new_slovar_ga = {
            "Код": 1,
            "Конкуренты": "Знак Майма",
            "Артикул": keys_ga,
            "Наименование": names_ga,
            "Вид цены": type_ga,
            "Цена": price_ga,
            "Ссылка": link_ga
        }

        df = pd.DataFrame(new_slovar)
        df2 = pd.DataFrame(new_slovar_ga)
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
            df2.to_excel(writer,
                        sheet_name="Майма",
                        index=False)
        else:
            with ExcelWriter(path, mode="w") as writer:
                df.to_excel(writer, sheet_name="Барнаул")
                df2.to_excel(writer, sheet_name="Майма")
        path = os.path.abspath("../Выгрузка цен Знак1.xlsx")
        end = time.time()
        print(end - start)


if __name__ == "__main__":
    znk = Znak()
    start = time.time()

    znk.gather_data_brn()
    znk.gather_data_ga()

    pool = Pool(processes=60)
    list_data = pool.starmap(znk.get_page_data_brn, znk.items)
    list_data_ga = pool.starmap(znk.get_page_data_ga, znk.items)
    znk.main(list_data,list_data_ga)
    end = time.time()
    print(end - start)

