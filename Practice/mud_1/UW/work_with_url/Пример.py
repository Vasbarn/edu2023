"""
pip install requests
import requests


headers = {
	'Referer': '',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers)

# изучить коды ответов

import json


value = {"Key": "Value"}

with open ("json_file.json", "w", encoding="utf-8") as file:
	x = json.dumps(value)
	print(x)


"""


