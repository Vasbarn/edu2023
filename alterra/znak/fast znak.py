import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(category=InsecureRequestWarning)
import asyncio
import aiohttp
import xlsxwriter
import datetime
import time

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
artix = []
articles = []
data = {}

async def get_page_data_brn(session, href, page):
    link = "https://znakooo.ru"+ href + f"?PAGEN_4={page}"
    print(link)
    async with session.get(link) as response:
        request = response.text
        soup = BeautifulSoup(await request(), "lxml")
        old_pr = soup.find_all(class_="name p-product__title")
        for op in old_pr:
            hrf = op.find("a").get("href")

            last_link = "https://znakooo.ru" + hrf
            response = await session.get(last_link)
            soup = BeautifulSoup(await response.text(), 'lxml')
            name = soup.find(class_="product-title").text
            cardprice = soup.find(class_="p-price p-price_strong").text.strip()
            type = soup.find(class_="p-price").text.strip()
            if "шт" in type:
                typing = "Цена ЗнакБарнаул за шт"
            elif "Уп" in type:
                typing = "Цена ЗнакБарнаул за Уп"
            elif "пог. м" in type:
                typing = "Цена ЗнакБарнаул за пог. м"
            article = soup.find_all(class_="product-characteristics")
            for art in article:
                a = art.find_all("span")
                artings = a[-1:]
                for val in artings:
                    data[val.text] = dict(Наименование=name, Цена_карта=cardprice, Цена=type[-11:], Ссылка=last_link,
                                            Единица_измерения=typing,
                                            Конкуренты="Знак Барнаул")

    print(data)
    # return data

# async def get_page_data_ga(session, href, page):
#     link = "https://galtaysk.znakooo.ru"+ href + f"?PAGEN_4={page}"
#     async with session.get(link) as response:
#         request = response.text
#         soup = BeautifulSoup(await request(), "lxml")
#         old_pr = soup.find_all(class_="name p-product__title")
#         for op in old_pr:
#             hrf = op.find("a").get("href")
#             last_link = "https://galtaysk.znakooo.ru" + hrf
#             response = await session.get(last_link)
#             soup = BeautifulSoup(await response.text(), 'lxml')
#             cardprice = soup.find(class_="p-price p-price_strong").text.strip()
#             type = soup.find(class_="p-price").text.strip()
#
#             if "шт" in type:
#                 types_ga.append("Цена ЗнакМайма за шт")
#             elif "Уп" in type:
#                 types_ga.append("Цена ЗнакМайма за Уп")
#             elif "пог. м" in type:
#                 types_ga.append("Цена ЗнакМайма за пог. м")
#             name = soup.find(class_="product-title").text



async def gather_data_brn():
    url = 'http://znakooo.ru/catalog/'
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        soup = BeautifulSoup(await response.text(), 'lxml')
        btn = soup.find_all(class_="collection")
        for group in btn:

            group_href = group.find("a").get("href").strip()
            x = url[:-9] + group_href
            response = await session.get(x)
            soup = BeautifulSoup(await response.text(), 'lxml')

            mxpgs = soup.find("div", class_="products__list products__list_e1").get("data-showmore").split(",")

            max_page = mxpgs[0]
            tasks =[]
            for i in range(1, int(max_page) + 1):
                task = asyncio.create_task(get_page_data_brn(session, group_href, i))
                tasks.append(task)

        await asyncio.gather(*tasks)

# async def gather_data_ga():
#     url = 'http://galtaysk.znakooo.ru/catalog/'
#     async with aiohttp.ClientSession() as session:
#         response = await session.get(url)
#         soup = BeautifulSoup(await response.text(), 'lxml')
#         btn = soup.find_all(class_="collection")
#         for group in btn:
#             group_href = group.find("a").get("href").strip()
#             x = url[:-9] + group_href
#             print(x)
#             response = await session.get(x)
#             soup = BeautifulSoup(await response.text(), 'lxml')
#             mxpgs = soup.find("div", class_="products__list products__list_e1").get("data-showmore").split(",")
#             max_page = mxpgs[0]
#             print(max_page)
#             tasks1 =[]
#         for i in range(1, int(max_page) + 1):
#             task = asyncio.create_task(get_page_data_ga(session, group_href, i))
#             tasks1.append(task)
#         await asyncio.gather(*tasks1)


def main():
    asyncio.run(gather_data_brn())
    # # asyncio.run(gather_data_ga())
    # for key, value in data.items():
    #     articles.append(key)
    #     names.append((data[key]["Наименование"]))
    #     linkages.append((data[key]["Ссылка"]))
    #     cardprices.append((data[key]["Цена_карта"]))
    #     prices.append((data[key]["Цена"]))
    #     types.append((data[key]["Единица_измерения"]))
    #
    new_slovar = {
        "Код": 1,
        "Конкуренты": "Знак Барнаул",
        "Артикул": articles,
        "Наименование": names,
        "Вид цены": types,
        "Цена": prices,
        "Цена по карте": cardprices,
        "Ссылка": linkages
    }
    # new_slovar_ga = {
    #     "Код": 1,
    #     "Конкуренты": "Знак Майма",
    #     "Артикул": "_",
    #     "Наименование": names_ga,
    #     "Вид цены": types_ga,
    #     "Цена": prices_ga,
    #     "Ссылка": linkages_ga}

    df = pd.DataFrame(new_slovar)
    # df2 = pd.DataFrame(new_slovar_ga)
    path = os.path.abspath("../Выгрузка цен Знак.xlsx")
    if os.path.exists(path):
        flag = open(path, "r")
        flag.close()
        os.remove(path)
        path = os.path.abspath("../Выгрузка цен Знак.xlsx")
        writer = pd.ExcelWriter("Выгрузка цен Знак.xlsx", engine="xlsxwriter")
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
    path = os.path.abspath("../Выгрузка цен Знак.xlsx")


# if __name__ == "__main__":
# 	while True:
# 		if datetime.datetime.now().hour == 7:
# main()
# 			time.sleep(60 * 60 * 24)
# 		time.sleep(60 * 20)


main()
