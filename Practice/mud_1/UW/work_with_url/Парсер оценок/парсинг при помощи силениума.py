from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tempfile
import zipfile
import requests
import os
import time

# def download_gcd():
#     href = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json'
#     response = requests.get(href)
#     for elem in response.json()["channels"]["Stable"]["downloads"]["chromedriver"]:
#         if elem.get("platform") == "win64":
#             href = elem.get("url")
#             response = requests.get(href)
#             break
#     with tempfile.TemporaryFile() as file:
#         file.write(response.content)
#         with zipfile.ZipFile(file) as fzip:
#             fzip.extractall(os.path.abspath(""))
#
# download_gcd()
service = ChromeService(os.path.join("chromedriver-win64", "chromedriver.exe"))
dr = webdriver.Chrome(service=service,)
dr.get("https://yandex.ru/maps/org/alterra/81604413003/?display-text=Альтерра&ll=83.917347%2C53.317547&mode=search&sll=83.881591%2C53.180441&sspn=0.118961%2C0.044344&text=%7B%22text%22%3A%22Альтерра%22%2C%22what%22%3A%5B%7B%22attr_name%22%3A%22chain_id%22%2C%22attr_values%22%3A%5B%22202774164838%22%5D%7D%5D%7D&z=11")
data = dr.page_source
print (data)
