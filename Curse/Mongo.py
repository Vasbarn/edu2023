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
id = []
end_prd=[]
strt_prd = []
r = open("all_info.xml", "r", encoding="utf-8")
xml_open = r.read()
soup = BeautifulSoup(xml_open,"lxml")
tbl_id = soup.findAll("tbl_id")
for elem in tbl_id:
    id.append(elem.text)
end = soup.findAll("end_prd")
for elem in end:
    end_prd.append(elem.text)
start = soup.findAll("strt_prd")
for elem in start:
    strt_prd.append(elem.text)
print(end_prd)
print(strt_prd)



# url = "https://opendata.1212.mn/api/Data?type=json"
# datas = {
# "tbl_id": "DT_NSO_2600_004V1",
#   "Period": [
#     "201701",
#     "201702",
#     "201703"
#   ]
# }
# resp = requests.post(url, json=datas)
# borsch = BeautifulSoup(resp.text, "lxml")
# print(borsch)



    

