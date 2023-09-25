"""
pip install requests
import requests


headers = {
	'Referer': '',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers)

# изучить коды ответов

import json


value = {"Key": "Value"}
"""

# import json
#
# # запись json
# value = {}
# with open ("json_file.json", "w", encoding="utf-8") as file:
# 	x = json.dumps(value, indent=4, ensure_ascii=False)
# 	print(x)
#
# # загрузка json
# with open("json_file.json", "r", encoding="utf-8") as file:
# 	data = json.load(file)
# print(data)
# print(data[0])

import requests
from bs4 import BeautifulSoup

response = requests.get("https://formulam2.ru/")
soup = BeautifulSoup(response.text, "lxml")
print(soup.find("div", class_="catalog-wrapper__content"))


m_dict = {"Артикул 123": {"Название": name, "Цена":price}}