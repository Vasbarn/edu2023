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

sys.setrecursionlimit(10000)


class Znak():
    def __init__(self):
       self.datas = dict()
       self.articles = list()
       self.types = list()
       self.items = []
    def get_page_data_brn(self, href, page):
        data = self.datas
        start = time.time()
        # link = "https://znakooo.ru/catalog/dveri/" + f"?PAGEN_4={page}"
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
                for val in artings:
                    self.articles.append(val.text)
            for arts, typing in self.articles, self.types:
                data[arts] = (last_link,name,price,cardprice, typing )
        return data

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

    # def gather_data_ga():
    #     url = 'http://galtaysk.znakooo.ru/catalog/'
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, 'lxml')
    #     btn = soup.find_all(class_="collection")
    #     for group in btn:
    #
    #         group_href = group.find("a").get("href").strip()
    #
    #         x = url[:-9] + group_href
    #         respon = requests.get(x)
    #         soup = BeautifulSoup(respon.text, 'lxml')
    #
    #         mxpgs = soup.find("div", class_="products__list products__list_e1").get("data-showmore").split(",")
    #
    #         max_page = mxpgs[0]
    #         for i in range(1, int(max_page) + 1):
    #             items_ga.append((group_href, i))
    #

    def main(self, x):



        dannye = dict()
        for elem in x:
            for key, item in elem.items():
                dannye[key] = item
        print(dannye)
        # new_slovar_ga = {
        #     "Код": 1,
        #     "Конкуренты": "Знак Майма",
        #     "Артикул": articles_ga,
        #     "Наименование": names_ga,
        #     "Вид цены": types_ga,
        #     "Цена": prices_ga,
        #     "Ссылка": linkages_ga
        # }

        # df = pd.DataFrame(new_slovar)
        # # df2 = pd.DataFrame(new_slovar_ga)
        # path = os.path.abspath("../Выгрузка цен Знак1.xlsx")
        # if os.path.exists(path):
        #     flag = open(path, "r")
        #     flag.close()
        #     os.remove(path)
        #     path = os.path.abspath("../Выгрузка цен Знак1.xlsx")
        #     writer = pd.ExcelWriter("Выгрузка цен Знак1.xlsx", engine="xlsxwriter")
        #     df.to_excel(writer,
        #                 sheet_name="Барнаул",
        #                 index=False)
        #     # df2.to_excel(writer,
        #     #             sheet_name="Майма",
        #     #             index=False)
        # else:
        #     with ExcelWriter(path, mode="w") as writer:
        #         df.to_excel(writer, sheet_name="Барнаул")
        #         # df2.to_excel(writer, sheet_name="Майма")
        # path = os.path.abspath("../Выгрузка цен Знак1.xlsx")
        # end = time.time()
        # print(end - start)


if __name__ == "__main__":
    znk = Znak()
    start = time.time()

    znk.gather_data_brn()
    # gather_data_ga()

    pool = Pool(processes=60)
    list_data = pool.starmap(znk.get_page_data_brn, znk.items)
    znk.main(list_data)
    # pool.starmap(get_page_data_ga,items_ga)
    end = time.time()
    print(end - start)

