import random
import time
import requests
from datetime import datetime
import os
import tempfile
import zipfile
import json
import pandas as pd
url = "https://znakooo.ru/"

response = requests.get(url, "lxml")
print(response)