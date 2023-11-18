import requests
from bs4 import BeautifulSoup
import json
from typing import Dict

# def parse():
response = requests.get("https://stopgame.ru/games/catalog")
soup = BeautifulSoup(response)
print(soup)

