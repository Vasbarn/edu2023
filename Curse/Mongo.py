import json

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from pandas.io.excel import ExcelWriter



ids = []
naming = []
trd_period = []
trd_volume = []
trd_helper = []
bal_period = []
bal_value = []
dt ={}
balance_data = {}
trd_data = {}
all_data = {}
tbl_list = []
r = open("all_info.xml", "r", encoding="utf-8")
xml_open = r.read()
soup = BeautifulSoup(xml_open,"lxml")
name = soup.findAll("tbl_eng_nm")
tbl_id = soup.findAll("tbl_id")
for names in name:
    naming.append(names.text)
for id in tbl_id:
    ids.append(id.text)
for i in range(len(naming)):
    dt[naming[i]]=ids[i]

tbl_list = ["DT_NSO_1400_003V1", "DT_NSO_0800_008V1"]
url = "https://opendata.1212.mn/api/Data?type=xml"
datas = {
    "tbl_id": "DT_NSO_1400_003V1",
#     "Period": ["2010"],
#     # "CODE": ["1"]
}
#
resp = requests.post(url, json=datas)
soup = BeautifulSoup(resp.text, "lxml")



periods = soup.findAll("period")
for elem in periods:
    trd_period.append(elem.text)
values = soup.findAll("dtval_co")
for elem in values:
    trd_volume.append(elem.text)
help = soup.findAll("scr_eng")
for elem in help:
    trd_helper.append(elem.text)
for i in range(0, len(trd_period), 4):
    trd_data[trd_period[i]] = trd_volume[i]
all_data["Внешнеторговый оборот"] = trd_data
periods = soup.findAll("period")
for elem in periods:
    bal_period.append(elem.text)
values = soup.findAll("dtval_co")
for elem in values:
    bal_value.append(elem.text)
for i in range(len(bal_period)):
    balance_data[bal_period[i]] = bal_value[i]
all_data["СБАЛАНСИРОВАННЫЙ БАЛАНС БЮДЖЕТА ОБЩЕГО УПРАВЛЕНИЯ"] = balance_data
print(all_data)

'FOREIGN TRADE MONTHLY TOTAL TURNOVER, EXPORT, IMPORT, by month: DT_NSO_1400_003V1'

'''DT_NSO_0800_008V1'''
    

