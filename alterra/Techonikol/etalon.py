import time

from alterra.parser import Parser
from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import datetime
import random


class ParserArsenal(Parser):
    def __init__(self, name: str):
        super().__init__(name)
        print(f"Загружаю {name} ")
        self.load_catalog()

    def load_catalog(self):
        """Парсим с главного сайта конкурента каталог товаров, и сохраняем его в атрибут self.__catalog"""
        catalog = dict()
        for _ in range(5):
            try:
                time.sleep(1)
                response = requests.get(self.main_url, headers=self.headers, timeout=20)
                break
            except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
                print("r", end="")
                continue
        else:
            return
        soup = BeautifulSoup(response.text, 'lxml')
        groups = soup.find_all(class_="catalog-dropdown-menu")
        for group in groups:
            name_group = group.find(class_="catalog_section__name").text.strip()
            href_group = group.find("a").get("href")
            href_group = href_group.split("/")
            href_group = "/".join(href_group[:-2]) + "/"
            href_group = self.main_url + href_group[1:]
            catalog[name_group] = href_group
        self.catalog = catalog


    def do_some(self, url: str):
        """Парсинг по конкретной странице"""
        for _ in range(5):
            try:
                response = requests.get(url, headers=self.headers, params={'paging': '48', 'viewType': 'list'},
                                        timeout=10)
                if response.status_code != 200:
                    time.sleep(random.randint(10, 30))
                    continue
                break
            except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
                print("r", end="")
                time.sleep(random.randint(5, 10))
                continue
            except:
                print("R", end="")
                time.sleep(random.randint(5, 10))
                continue
        else:
            return
        soup = BeautifulSoup(response.text, "lxml")
        max_page = soup.find(class_="bx-pagination")
        if max_page is None:
            max_page = 1
        else:
            max_page = max_page.find_all("li")
            max_page = int(max_page[-2].text.strip())
        data = self.data
        for page in range(1, max_page + 1):
            goods = soup.find_all(class_="product-block")
            for good in goods:
                href = self.main_url + good.find(target="_self").get("href")[1:]

                name = good.find(class_="description").find("a").text.strip()
                article = good.find(class_="description").find("span")
                article = article.text.replace("\t", "")
                article_list = article.split("\n")
                for elem in article_list:
                    if "Артикул" in elem:
                        article = elem.replace("Артикул:", "").strip()
                list_price_name = good.find_all(class_="price-name")
                list_price = good.find_all(class_="js-value")
                list_unit = good.find_all(class_="unit")
                for num in range(len(list_price_name)):
                    price_name = list_price_name[num].text.strip()
                    price = round(float(list_price[num].text.strip().replace(" ", "")), 2)
                    unit = list_unit[num].text.strip().replace("/", "")
                    price_name = f"{self.name} {price_name} за {unit}"
                    if data.get(article):
                        article += " "
                    data[article] = (str(self.name).strip(),
                                     str(article).strip(),
                                     str(name).strip(),
                                     str(price_name).strip(),
                                     str(price).strip(),
                                     str(href).strip(),
                                     "01-01028075")
            if page + 1 < max_page + 1:
                new_url = url + f"?paging=96&PAGEN_1={page + 1}&viewType=list"
                for _ in range(10):
                    try:
                        time.sleep(1)
                        response = requests.get(new_url, headers=self.headers, timeout=20)
                        soup = BeautifulSoup(response.text, "lxml")
                        if response.status_code != 200:
                            time.sleep(random.randint(10, 30))
                            continue
                        break
                    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
                        print("r", end="")
                        time.sleep(random.randint(5, 10))
                        continue
                    except:
                        print("R", end="")
                        time.sleep(random.randint(5, 10))
                        continue
                else:
                    return
        print("#", end="")
        return data

    def do_all(self):
        """Парсинг по всем страницам"""
        print(f"Процесс {self.name} (всего групп {len(self.catalog.values())}):", end=" ")
        p = Pool(processes=1)
        list_data = p.map(self.do_some, self.catalog.values())
        data = dict()
        for some_dir in list_data:
            for key, item in some_dir.items():
                data[key] = item
        self.data = data
        print("\r", end="")

