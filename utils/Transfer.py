from datetime import datetime as date
import os
import json
from utils.get_sorted_transfers import get_sorted_transfers


class Transfer:
    def __init__(self):
        self.list_transfer = []

    def __repr__(self):
        return (f"Return file with informstion\n"
                f"about user:\n"
                f"{self.list_transfer}\n")

    def get_list_transfer(self):
        with open(os.path.join('..', 'data', 'operations.json'), 'r', encoding='UTF-8') as list_data:
            self.list_transfer = json.loads(list_data.read().strip())
        return self.list_transfer

    def get_last_info(self):
        get_sorted_transfers(self.list_transfer)
        sorted_list = self.list_transfer
        list_info = []
        len_list_info = len(list_info)

        while len_list_info < 6:

            for info in range(len(sorted_list) - 1):

                date_str = sorted_list[info].get('date')
                date_class = date.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
                date_formatted = date_class.strftime("%d.%m.%Y")

                list_info.extend([date_formatted, sorted_list[info]['description'],
                                  sorted_list[info]['from'], '->', sorted_list[info]['to'],
                                  sorted_list[info]['operationAmount']['amount'],
                                  sorted_list[info]['operationAmount']['currency']['name']])
                return list_info


x = Transfer()
x.get_list_transfer()

print(x.get_last_info())
