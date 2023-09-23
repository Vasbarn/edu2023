import requests
from bs4 import BeautifulSoup
import json
listing = ("https://formulam2.ru/catalog/01_sukhie_smesi_teploizolyatsiya_gipsokarton/sukhie_stroitelnye_smesi/shpaklevka/shpaklevka_gotovaya/shpatlevka_finishnaya_polimernaya_uni_pasta_25_kg_bergauf_bergauf/", "https://formulam2.ru/catalog/02_lakokrasochnye_materialy/kolery_dlya_kraski/pasta_kolerovochnaya_universal_0_1_l_kofeynyy_teks/", "https://formulam2.ru/catalog/02_lakokrasochnye_materialy/kolery_dlya_kraski/pasta_kolerovochnaya_parade_246_zelenoe_yabloko_0_25l_rossiya_0005812/", "https://formulam2.ru/catalog/07_napolnye_pokrytiya/plitka_pvkh_i_spc/spirit_home/plitka_pvkh_spirit_home_30_gd_grace_natural_60001349_1219kh184kh2_15sht_3_364_kv_m/")
response = requests.get("https://formulam2.ru/catalog/01_sukhie_smesi_teploizolyatsiya_gipsokarton/sukhie_stroitelnye_smesi/shpaklevka/shpaklevka_gotovaya/shpatlevka_finishnaya_polimernaya_uni_pasta_25_kg_bergauf_bergauf/")
print(response.status_code)
soup = BeautifulSoup(response.text, "lxml")
name = soup.find(class_ = "product-detail__title").text
price = soup.find(class_ = "product-info__content-main").text
price = float(price.replace("   ₽ / шт", '').replace(" ",''))
article = soup.find(class_ = "product-detail__code-number").text.strip()
adress = soup.find(class_ = "")

slovar = dict()
slovar[article] = {"Название": name, "Цена": price}

for url in listing:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    name = soup.find(class_="product-detail__title").text
    price = soup.find(class_="product-info__content-main").text
    # price = float(price.replace("₽ / шт", '').replace(" ", ''))
    article = soup.find(class_="product-detail__code-number").text.strip()
    adress = soup.find(class_="")
    slovar[article] = {"Название": name, "Цена": price}
with open("myJson.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(slovar, ensure_ascii=False, indent=4))
