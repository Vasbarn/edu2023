from alterra.sdfgfrgfvedbg import ParserFormulaM2
import os
import time
from datetime import datetime

def main():

    try:
        try_num = 0
        flag = True
        while try_num < 5 and flag:
            time_start = time.time()
            parser_formulam2 = ParserFormulaM2("ФормулаМ2Барнаул")
            work(parser_formulam2)
            finish_time = time.time()
            if finish_time - time_start < 60:
                try_num += 1
            else:
                flag = False
    except Exception as error:
        print(error)


def work(var_cls):

	# path = os.path.abspath(os.path.join("", "Выгрузки"))
	var_cls.do_all()


	var_cls.safe_data_to_file("Выгрузка цен.xlsx")


if __name__ == "__main__":
	main()


