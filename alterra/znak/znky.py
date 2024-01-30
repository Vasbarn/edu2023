from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import pandas as pd
import os
from pandas.io.excel import ExcelWriter
from openpyxl import *





class ParserTechnonikol():
    def __init__(self):
        self.url = "https://znakooo.ru/catalog/"
        self.url_g = "https://galtaysk.znakooo.ru/catalog/"
        self.catalog_url = []
        self.max_page = []
        self.group_name = []
        self.products_by_page={}
        self.driver = webdriver.Chrome()
        self.browser = self.driver.page_source
        self.new_url = []
        self.full_links = []
        self.prices = []
        self.type = []
        self.cardprices = []
    def get_catalog(self):

        self.driver.get(self.url)
        soup = BeautifulSoup(self.browser, "lxml")
        groups = soup.find_all(class_="collection")
        print("zdess")
        for group in groups:
            group_href = group.find("a").get("href")
            print("zdess")
            self.catalog_url.append(self.url[:-9] + group_href)


    def get_max_page(self):

        for urls in self.catalog_url[:1]:
            self.driver.get(urls)
            soup = BeautifulSoup(self.browser, 'lxml')
            max_pgs = soup.find("div", class_="products__list products__list_e1").get("data-showmore").split(",")
            max_page = max_pgs[0]
            print("zdess 2")
            for i in range(2, int(max_page) + 1):
                link = urls + f"?PAGEN_4={i}"
                self.new_url.append(link)


    def get_product_info(self):

        for elem in self.new_url:
            self.driver.get(elem)
            soup = BeautifulSoup(self.browser, "lxml")
            old_price = soup.find_all(class_="name p-product__title")
            for op in old_price:
                hrf = op.find("a").get("href")
                self.full_links.append(self.url[:-9] + hrf)
                print("zdess 3")
            for link in self.full_links:
                self.driver.get(link)
                soup = BeautifulSoup(self.browser, 'lxml')
                cardprice = soup.find(class_="p-price p-price_strong").text.strip()
                price = soup.find(class_="p-price").text
                self.cardprices.append(cardprice)
                self.type.append(price[14:].strip())
                print(self.type)
                self.prices.append(price[:-11])
    def write_in_file(self):
        pass


x = ParserTechnonikol()
x.get_catalog()
x.get_max_page()
x.get_product_info()


