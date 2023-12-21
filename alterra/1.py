from bs4 import BeautifulSoup
import requests
import lxml
import json



url = "https://gorniy.formulam2.ru/"


def get_main_link(url: str, slovar: dict):
    slovar["Link"] = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    division = soup.find_all(class_="catalog__list-item depth_level_1")
    for sub_div in division:
        href = sub_div.find_all("a")
        for good_pg in href:
            good = good_pg.get("href")
            slovar["Link"].append(url+good)
    return slovar['Link']

def get_goods_info(borsch: "BeautifulSoup", slovar: dict):
    print(borsch)
    way = borsch.find("div", class_="product-card__img").find("a").get("href")
    name = borsch.find("div", class_="js-toclamp-4").text
    art = borsch.find("div", class_ = "product-card__index")
    price = borsch.find("div", class_="product-card__new-price").find("span").text
    quantity = borsch.find("div", class_="product-card__new-price").text.split("/")[1]
    slovar["Ссылка на товар"] = way
    slovar["Наименование"] = name
    slovar["Артикул"] = art
    slovar["Цена"] = price
    slovar["Единица измерения"] = "Цена ФормулаМ2Горный за" + quantity

def get_pages(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    try:
        max_page = int(soup.find_all(class_="pagination__link")[-1].text.strip())
    except (IndexError, TypeError):
        max_page = 1
    return max_page



slovar={}
quantity = get_main_link(url, slovar)
for x in range(len(quantity) + 1):
    pages = get_pages(slovar["Link"][x])
    for page in range(1, pages+1):
        response = requests.get(f'{slovar["Link"][x]}?PAGEN_1={page}')
        soup = BeautifulSoup(response.text, "lxml")
        goods = soup.find_all("div", class_="products-grid__row")
        for good in goods:
            get_goods_info(good, slovar)
        print(page)
        print(str(page) + "/" + str(pages), end="\r")


with open("Parser_mount.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(slovar, ensure_ascii=False, indent=4))





