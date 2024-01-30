import random
import time
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

url = "https://znakooo.ru/catalog/"
response = requests.get(url, verify=False)
max_pg=[]
catalog_url = []
new_url = []
linkages = []
type=[]
prices = []
names = []
soup = BeautifulSoup(response.text, 'lxml')
btn = soup.find_all(class_="collection")
for group in btn:
    group_href = group.find("a").get("href").strip()
    catalog_url.append(url[:-9] + group_href)
for urls in catalog_url:
    response = requests.get(urls, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    mxpgs = soup.find("div",class_="products__list products__list_e1").get("data-showmore").split(",")
    max_page = mxpgs[0]
    for i in range(2, int(max_page)+1):
        link = urls + f"?PAGEN_4={i}"
        new_url.append(link)
    for elem in new_url:
        response = requests.get(elem, verify=False)
        soup = BeautifulSoup(response.text, "lxml")
        old_pr = soup.find_all(class_="name p-product__title")
        for op in old_pr:
            hrf = op.find("a").get("href")
            linkages.append(url[:-9]+hrf)
    for zet in linkages:
        response = requests.get(zet, verify=False)
        soup = BeautifulSoup(response.text, 'lxml')
        cardprice = soup.find(class_="p-price p-price_strong").text.strip()
        pric = soup.find(class_="p-price").text
        name = soup.find(class_="product-title").text
        print(name)
        names.append(name)
        type.append(pric[14:].strip())
        prices.append(pric[:-11])
print(names)
print(type)
print(prices)






