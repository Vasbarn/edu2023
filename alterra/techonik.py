import requests
from bs4 import BeautifulSoup

from alterra.parser import Parser
from typing import Dict
import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from openpyxl import *
import os

from selenium.webdriver.common.by import By
import time
import requests
import fake_user_agent
#from bs4 import BeautifulSoup

from selenium import webdriver
driver = webdriver.Chrome()

session = requests.Session()
url = 'https://barnaul.tstn.ru/shop/krovelnye-materialy/'

driver.get(url)

# x = driver.find_element(By.XPATH,"b-catalog__body")
html = driver.page_source
soup = BeautifulSoup(html,"lxml")
print(soup.prettify())

