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

datas = {}
r = open("all_info.xml", "r", encoding="utf-8")
xml_open = r.read()
soup = BeautifulSoup(xml_open,"lxml")
z = soup.findAll("tbl_id")
for elem in z:
    print(elem.text)





    

