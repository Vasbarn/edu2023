import fake_user_agent
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from pandas import DataFrame
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

url = 'https://znakooo.ru/catalog/'
driver = webdriver.Chrome()
driver.get(url)
vf = driver.page_source
soup = BeautifulSoup(vf,"lxml")
print(soup)
#

# user = fake_user_agent.user_agent()
# headers = {
#     'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
#                    'Firefox/14.0.1')}
# data = {
#     "USER_LOGIN": "ЛОГИН",
#     "USER_PASSWORD": "ПАРОЛЬ"
# }
# #
# responce = session.post(
#     url,
#     data=data,
#     headers=headers,
#     verify=False
# )
# print(responce)


# max_pg=[]
# catalog_url = []
# new_url = []
# linkages = []
# type=[]
# prices = []
# names = []
# response = requests.get(url, verify=False)
# soup = BeautifulSoup(response.text, 'lxml')
# btn = soup.find_all(class_="collection")
#
# for group in btn:
#     print(group.text)
#     group_href = group.find("a").get("href").strip()
#     catalog_url.append(url[:-9] + group_href)
# for urls in catalog_url:
#
#     response = requests.get(urls, verify=False)
#
#     soup = BeautifulSoup(response.text, 'lxml')
#     mxpgs = soup.find("div",class_="products__list products__list_e1").get("data-showmore").split(",")
#     max_page = mxpgs[0]
#     for i in range(2, int(max_page)+1):
#         link = urls + f"?PAGEN_4={i}"
#         new_url.append(link)
#         for elem in new_url:
#             print(elem)
#             response = requests.get(elem, verify=False)
#
#             soup = BeautifulSoup(response.text, "lxml")
#             old_pr = soup.find_all(class_="name p-product__title")
#             for op in old_pr:
#
#                 hrf = op.find("a").get("href")
#                 linkages.append(url[:-9]+hrf)
#             for link in linkages:
#                 response = requests.get(link, verify=False)
#                 print(3, link)
#                 soup = BeautifulSoup(response.text, 'lxml')
#                 cardprice = soup.find(class_="p-price p-price_strong").text.strip()
#                 types = soup.find(class_="p-price").text
#                 name = soup.find(class_="product-title").text
#                 print(name)
#
#                 names.append(name)
#                 type.append(types[14:].strip())
#                 prices.append(types[:-11])
# # print(names)
# print(type)
# print(prices)

# new_slovar = {
#     "Код": 1,
#     "Конкуренты": "ЗнакБарнаул",
#     "Артикул": '',
#     "Наименование": names,
#     "Вид цены": type,
#     "Цена": prices,
#     "Ссылка": linkages
# }
# df = DataFrame(new_slovar)
# path = os.path.abspath("C:\\Users\\Admin\\PycharmProjects\\edu2023\\alterra\\Выгрузка цен Знак.xlsx")
# if os.path.exists(path):
#     flag = open(path, "r")
#     flag.close()
#     os.remove(path)
#     path = os.path.abspath("../Выгрузка цен (4).xlsx")
#     df.to_excel("C:\\Users\\Admin\\PycharmProjects\\edu2023\\alterra\\Выгрузка цен (4).xlsx", sheet_name="Лист 1", index=False)
# else:
#     with ExcelWriter(path, mode="w") as writer:
#         df.to_excel(writer, sheet_name="Лист 1")






