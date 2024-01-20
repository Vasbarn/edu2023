import random
import time

from alterra.parser import Parser
import requests
from datetime import datetime
import os
import tempfile
import zipfile
import json
import pandas as pd


class ParserLeroyMerlin(Parser):
    def __init__(self, name: str, download_mark: bool = False):
        super().__init__(name)
        print(f"Загружаю {name} ")

        # Загрузить католог из файла? если да, то берем готовый, если нет, то собираем новый.
        if download_mark:
            with open(os.path.abspath(os.path.join("Parsers", "../Helpers/catalog_lm.json")), "r",
                      encoding="utf-8") as file:
                self.catalog = json.load(file)
                print()
        else:
            # options = webdriver.ChromeOptions()
            # options.headless = False
            # options.add_experimental_option('excludeSwitches', ['enable-logging'])
            # options.add_experimental_option('useAutomationExtension', False)
            # options.add_argument("user-agent={}".format(self.headers))
            # options.add_argument("--disable-blink-features=AutomationControlled")
            # service = ChromeService(os.path.join("chromedriver-win64", "chromedriver.exe"))
            # with webdriver.Chrome(service=service,
            #                       options=options) as driver:
            #     driver.get(url="https://barnaul.leroymerlin.ru/content/elbrus/barnaul/ru/catalogue.navigation.json")
            #     qrator_ssid = driver.get_cookie("qrator_ssid")
            #     cook = {"qrator_ssid": qrator_ssid.get("value")}

            self.load_catalog(
                url="https://barnaul.leroymerlin.ru/content/elbrus/barnaul/ru/catalogue.navigation.json")
            catalog = json.dumps(self.catalog, indent=1, ensure_ascii=False)
            with open(os.path.abspath(os.path.join("Parsers", "../Helpers/catalog_lm.json")), "w",
                      encoding="utf-8") as file:
                file.write(catalog)
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            # 'Cookie': 'iap.uid=0c8ea8b277b0414687715cf5c16c67c7; _ym_uid=1665709049978836832; uxs_uid=2f027230-4b5b-11ed-a5e6-7535f65cfc06; cookie_accepted=true; ggr-widget-test=1; _ym_d=1684117566; aplaut_distinct_id=l15vMZ6DoLhb; adrcid=AB-yEYcaE0_L1EnbYlpsolQ; _ym_isad=2; tmr_lvid=a7450aa218fbc62926002c0810857358; tmr_lvidTS=1665709049592; _clientTypeInBasket=true; _singleCheckout=true; _unifiedCheckout=true; _gid=GA1.2.1358987194.1684387034; lastConfirmedRegionID=34; qrator_jsid=1684458405.713.15Gt7slyaGbChjZM-s0blt8q4o7dgdcf1s879hjdu9sjcaivp; GACookieStorage=GA1.2.2090868684.1665709048; x-api-option=srch-2705; adrdel=1; sawOPH=true; _slfs=1684458414945; X-API-Experiments-sub=B; _slid=6466cbafc4dc52af18021e62; _slsession=1AF84F65-6BD5-4C8B-B9E9-B7B4CBF4AE77; _slid_server=6466cbafc4dc52af18021e62; _gat_UA-20946020-1=1; _regionID=2397; _reactCheckout=true; _b2bCheckout3=true; _gaexp=GAX1.2.IUgFRjY7S7qnkK4uRsCZRw.19540.3!cZIZVorfRoerwcLCKkVpYQ.19586.x525!UuMasWCuTGGveYXojQKTqg.19518.2; _deliveryTerms=v2; _ga=GA1.2.2090868684.1665709048; _ga_Z72HLV7H6T=GS1.1.1684458408.5.1.1684458857.0.0.0',
            'Origin': 'https://barnaul.leroymerlin.ru',
            'Referer': 'https://barnaul.leroymerlin.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-api-key': 'Yeg8l3zQDwpVNBDTP3q6jM4lQVLW5TTv',

        }

    def load_catalog(self, url=None, cook=None):
        """
        Парсим с главного сайта конкурента каталог товаров, и сохраняем его в атрибут self.__catalog
        Рекурсивно проходим до внутренних групп, и берем самые крайние,
        так как товар не всегда входит в вышестоящие группы.
        Требуется только юзер-агент
        """
        my_try = 0
        while True:
            if my_try > 5:
                return
            try:
                response = requests.get(url, headers=self.headers, cookies=self.cookies, timeout=10)
                if response.status_code != 200:
                    my_try += 1
                    print("${}\n{}\n{}".format(response.status_code, url, response.text), end="")
                    if my_try > 5:
                        return
                    time.sleep(random.randint(30, 60))
                    continue
                print(".", end="")
                data = response.json()
                self.save_group(data)
                break
            except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
                time.sleep(3)
                my_try += 1
                print("r", end="")
                continue


