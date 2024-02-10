import urllib3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(category=InsecureRequestWarning)
import asyncio
import aiohttp

artix = []
arr = []
llink= ["http://znakooo.ru/catalog/santekhnika/vanny_i_komplektuyushchie/vanna_akrilovaya_sofa_170x70_s_karkasom_bez_paneli/",
        "https://znakooo.ru/catalog/stroymaterialy/profili_i_komplektuyushchie_dlya_gkl/steklosetki_serpyanki_lenty/lenta_serpyanka_48mm_kh_90m/",
        "https://znakooo.ru/catalog/elektrotovary/kabel_provod_elektromontazh/komplektuyushchie_dlya_elektromontazha/nakonechnik_nki_2_6_koltso_1_5_2_5mm/"]
for l in llink:
    response = requests.get(l, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    article = soup.find_all(class_="product-characteristics")
# print(article)
    for art in article:
        a = art.find_all("span")
        z = a[-1:]

        for x in z:
            print(x.text)


# artix.append(article)
# print(artix)