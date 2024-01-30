import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import requests
import fake_user_agent

session = requests.Session()
url = "https://znakooo.ru/"
user = fake_user_agent.user_agent()
headers = {
    "User-Agent": user
}

data = {
    "USER_LOGIN": "ЛОГИН",
    "USER_PASSWORD": "ПАРОЛЬ"
}

responce = session.post(
    url,
    data=data,
    headers=headers
)
print(responce)

main_url ="https://znakooo.ru/"
main_responce = session.get(main_url, headers=headers).text

print(main_responce)

