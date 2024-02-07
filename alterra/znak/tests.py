from alterra.Parser import Parser
from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import time
import random

class ParserZnak(Parser):
    def __init__(self, name: str):
        super().__init__(name)
        print(f"Загружаю {name}")
        self.load_catalog()


    def load_catalog(self):

        catalog = dict()
        for _ in range(5):
            try:
                response = requests.get(self.main_url, headers=self.headers, timeout=10, verify= False)
                soup = BeautifulSoup(response.text, 'lxml')
                groups_goods = soup.find_all(class_="collection")
                for group_good in groups_goods:
                    href = group_good.find("a").get("href")
                    if not href:
                        continue
                    href = self.main_url[:-9] + href
                    name_group = group_good.text.strip()
                    catalog[name_group] = href
                self.catalog = catalog
            except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
                print("r", end="")
                continue
        else:
            return

    def do_some(self, url: str):
        """Парсинг по конкретной странице"""
        global name, article, price_name, price, href, card_price
        for _ in range(5):
            try:
                response = requests.get(url, headers=self.headers, cookies={'setqty': '100'}, timeout=10)
                if response.status_code != 200:
                    time.sleep(random.randint(10, 30))
                    continue
                break
            except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
                print("r", end="")
                time.sleep(random.randint(5, 10))
                continue
        else:
            return
        soup = BeautifulSoup(response.text, "lxml")
        data = self.data
        self.linkages = []
        linkages = self.linkages
        try:
            pages = soup.find("div",class_="products__list products__list_e1").get("data-showmore").split(",")
            if pages is None:
                max_page = 1
            else:
                max_page = pages[0]
            for page in range(max_page + 1):
                for elem in self.catalog:
                    link = elem + f"?PAGEN_4={page}"
                    response = requests.get(link, verify = False)
                    soup2 = BeautifulSoup(response.text, "lxml")
                    all_href = soup2.find_all(class_="name p-product__title")
                    for hrf in all_href:
                        product_href = hrf.find("a").get("href")
                        linkages.append(url[:-9] + hrf)
                        for link in linkages:
                            response = requests.get(link, verify=False)
                            soup3 = BeautifulSoup(response.text, 'lxml')
                            href = link
                            name = soup3.find(class_="product-title").text.strip()
                            article = 1
                            price = soup3.find(class_="p-price").text
                            card_price = soup3.find(class_="p-price p-price_strong").text.strip()
                            unit,price = price[14:], price[:-11]
                            price_name = f"Цена {self.name} за {unit}"
                    # if self.name == "ФормулаМ2Барнаул":
                    data[article] = (self.name, article, name, price_name, price,card_price, href)
                    # elif self.name == "ФормулаМ2Бийск":
                    # 	data[article] = (self.name, article, name, price_name, price, href, "01-01028089")


            print(1, end="")
        except TimeoutError as error:
            print(error, end="")
        finally:
            return data

    def do_all(self):
        """Парсинг по всем страницам"""

        print(f"Процесс {self.name} (всего групп {len(self.catalog.values())}):", end=" ")
        p = Pool(processes=len(self.catalog.values()))
        list_data = p.map(self.do_some, self.catalog.values())
        data = dict()
        for some_dir in list_data:
            for key, item in some_dir.items():
                data[key] = item
        self.data = data
        print("\r", end="")
