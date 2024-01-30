import os
import pandas as pd
import ExcelWriter
from typing import Dict, Any, Tuple
from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс парсер"""
    def __init__(self, name: str):
        """
        Создается экземпляр класс парсер с именем и путем к файлу со ссылкой на сайт конкурента.
        :param name: наименование парсера, должна точно соответствовать одному из значений книги xlsx
        :param path_to_file: путь к книге xlsx
        """
        self.name = name
        self.__main_url = self._get_main_url()
        self.__catalog = dict()
        self.__data = dict()
        self.__headers =\
            {
                'Accept': '*/*',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
             }
        self.__cookies = {}

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Название парсера может быть только строкой!")

    @property
    def main_url(self) -> str:
        return self.__main_url

    @property
    def catalog(self) -> Dict[str, str]:
        """Получить список номенклатурных групп конкурента"""
        return self.__catalog

    @catalog.setter
    def catalog(self, list_dict: Dict[str, str]):
        """Залить список группа номенклатур конкурента"""
        if isinstance(list_dict, dict):
            self.__catalog = list_dict
        else:
            raise TypeError("Каталог должен быть  словарем!")




    def safe_data_to_file(self, full_name: str, message_mark: bool = False):
        """Сохранение словаря self.__data в книгу xlsx по указанному пути"""
        parts_path = full_name.split(os.sep)
        if not os.path.exists(os.sep.join(parts_path[:-1])):
            os.mkdir(os.sep.join(parts_path[:-1]))
        df = pd.DataFrame()
        df["Код"] = ""
        df["Конкурент"] = ""
        df["Артикул"] = ""
        df["Наименование"] = ""
        df["Вид цены"] = ""
        df["Цена"] = ""
        df["Ссылка"] = ""
        try:
            for key, item in self.data.items():
                df.loc[len(df)] = (str(item[6]), str(item[0]), str(item[1]).strip(), str(item[2]), str(item[3]),
                                   str(item[4]),
                                   str(item[5]))
            writer = pd.ExcelWriter(full_name)
            df.to_excel(writer, sheet_name="Данные", index=False)
            writer.save()
            if message_mark:
                print("Данные по {} сохранены в {}".format(self.name, full_name))
        except PermissionError:
            print("Не могу сохранить данные, в файл. Так как он открыт! {}".format(self.name))

