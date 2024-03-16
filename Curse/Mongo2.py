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

tbl_list = ["DT_NSO_0300_027V1", "DT_NSO_0800_008V1"]
url = "https://opendata.1212.mn/api/Data?type=json"
url2 = "https://opendata.1212.mn/api/Data?type=json"

datas = {
    "tbl_id": "DT_NSO_1700_002V1",
    # "Period": ["201506", "201505"]
}

resp = requests.post(url, json=datas)
soup = BeautifulSoup(resp.text, "lxml")
print(soup)

# periods = soup.findAll("period")
# for elem in periods:
#     trd_period.append(int(elem.text))
# values = soup.findAll("dtval_co")
# for elem in values:
#     trd_volume.append(float(elem.text))
# for i in range(0, len(trd_period), 4):
#     trd_data[trd_period[i]] = trd_volume[i]
# all_data["Внешнеторговый оборот"] = trd_data

