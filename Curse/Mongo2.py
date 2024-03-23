from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup
import pandas as pd
import statistics
import scipy
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

ids = []
naming = []
ws_regions = []
water_val = []
water_obj = []
unique_rg = []
balance_data = {}
trd_data = {}
all_data = {}

tbl_list = ["DT_NSO_0300_027V1", "DT_NSO_1700_002V1"]
url = "https://opendata.1212.mn/api/Data?type=xml"
url2 = "https://opendata.1212.mn/api/Data?type=json"

datas = {
    "tbl_id": "DT_NSO_0700_021V1" ,
    "Period": ["2010"]
}

resp = requests.post(url, json=datas)
soup = BeautifulSoup(resp.text, "lxml")
# print(soup)
regions = soup.findAll("scr_eng1")
for elem in regions:
    ws_regions.append(elem.text)
print(ws_regions)
# # print(list(set(trd_period)))
# [unique_rg.append(x) for x in ws_regions if x not in unique_rg]
# print(unique_rg)
# div = soup.findAll("scr_eng")
# for elem in div:
#     water_obj.append(elem.text)
# print(set(water_obj))
# values = soup.findAll("dtval_co")
# for elem in values:
#     water_val.append(elem.text)
# print(trd_volume)
# for i in range(0, len(trd_period), 4):
#     trd_data[trd_period[i]] = trd_volume[i]
# all_data["Внешнеторговый оборот"] = trd_data


