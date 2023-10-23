from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tempfile
import zipfile


def download_gcd():
    href = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json'
    response = requests.get(href)
    for elem in response.json()["channels"]["Stable"]["downloads"]["chromedriver"]:
        if elem.get("platform") == "win64":
            href = elem.get("url")
            response = requests.get(href)
            break
    with tempfile.TemporaryFile() as file:
        file.write(response.content)
        with zipfile.ZipFile(file) as fzip:
            fzip.extractall(os.path.abspath(""))



# ptions = webdriver.ChromeOptions()
# options.headless = True
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("user-agent={}".format(self.headers))
# options.add_argument("--disable-blink-features=AutomationControlled")
with webdriver.Chrome(executable_path=os.path.join("chromedriver-win64", "chromedriver.exe")) as driver:
	driver.get(url)