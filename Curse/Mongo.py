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
bal_period = []
bal_value = []
loyal_period = []
loyal_value = []
loyal_data = {}
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
url = "https://opendata.1212.mn/api/Data?type=json"
datas = {
    "tbl_id": "DT_NSO_1400_003V1",
}
datas1 = {
    "tbl_id": "DT_NSO_0800_008V1",
}
datas2 = {
    "tbl_id": "DT_NSO_0700_010V1",
    # "Period": ["201506", "201505"]
}
resp = requests.post(url, json=datas)
soup = BeautifulSoup(resp.text, "lxml")

# print(soup)
resp1 = requests.post(url, json=datas1)
soup1 = BeautifulSoup(resp1.text, "lxml")

resp2 = requests.post(url, json=datas2)
soup2 = BeautifulSoup(resp2.text, "lxml").text
print(soup2.split("Total liabilities"))

#
# periods = soup.findAll("period")
# for elem in periods:
#     trd_period.append(elem.text)
# values = soup.findAll("dtval_co")
# for elem in values:
#     trd_volume.append(elem.text)
# for i in range(0, len(trd_period), 4):
#     trd_data[trd_period[i]] = trd_volume[i]
# all_data["Внешнеторговый оборот"] = trd_data
#
# periods = soup1.findAll("period")
# for elem in periods:
#     bal_period.append(elem.text)
# values = soup1.findAll("dtval_co")
# for elem in values:
#     bal_value.append(elem.text)
# for i in range(len(bal_period)):
#     balance_data[bal_period[i]] = bal_value[i]
# all_data["Баланс бюджета общего управления"] = balance_data
#
# periods = soup2.findAll("period")
# for elem in periods:
#     loyal_period.append(elem.text)
# values = soup2.findAll("dtval_co")
# for elem in values:
#     loyal_value.append(elem.text)
# for i in range(11, len(loyal_period), 10):
#     # loyal_data[loyal_period[i]] = loyal_value[i]
#     print(loyal_value[i])
# print(loyal_data)
# all_data["Общие обязательства"] = loyal_data
# df = pd.DataFrame(all_data)
# print(df)



    

