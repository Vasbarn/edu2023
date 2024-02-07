import os
import time
from datetime import datetime

from alterra.znak.tests import ParserZnak
def main():
	try:
		parser_znaak = ParserZnak("Знак")
		work(parser_znaak)
	except Exception as error:
		print(error)

def work(var_cls):
	var_cls.safe_data_to_file("Выгрузка цен5.xlsx")


if __name__ == "__main__":
	main()
	# while True:
	# 	if datetime.now().hour == 10:
	# 		print(datetime.now())
	# 		main()
	# 		print(datetime.now())
	# 		time.sleep(60 * 60 * 3)
	# 	time.sleep(60 * 15)
