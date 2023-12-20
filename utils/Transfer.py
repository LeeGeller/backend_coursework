from datetime import datetime as date
import os
import json
from utils.get_sorted_transfers import get_sorted_transfers


class Transfer:
    def __init__(self):
        self.list_transfer = []
        self.last_info = []

    def __repr__(self):
        return (f"Return file with informstion\n"
                f"about user:\n"
                f"{self.list_transfer}\n"
                f"Return last transfers:\n"
                f"{self.last_info}")

    def get_list_transfer(self):
        with open(os.path.join('..', 'data', 'operations.json'), 'r', encoding='UTF-8') as list_data:
            self.list_transfer = json.loads(list_data.read().strip())
        return self.list_transfer

    def get_last_info(self, sorted_list):
        list_info = []

        for i in range(6):
            if sorted_list[i].get('from'):
                date_str = sorted_list[i].get('date')
                date_class = date.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
                date_formatted = date_class.strftime("%d.%m.%Y")

                last_info = (f"{date_formatted} {sorted_list[i]['description']} "
                             f"{sorted_list[i]['from']} -> {sorted_list[i]['to']} "
                             f"{sorted_list[i]['operationAmount']['amount']} {sorted_list[i]['operationAmount']['currency']['name']}")
                list_info.append(last_info.replace('\n', ''))

        return '\n'.join(list_info)

    def code_check_to(self, sorted_list):
        for i in range(6):
            if sorted_list[i].get('from'):
                str_info = sorted_list[i].get('from')
                list_info = str_info.split()
                number = list_info[1]
                code_formatted = f'{number[:4]} {number[4:6]}** ****{number[12:]}'
                return code_formatted


x = Transfer()
x.get_list_transfer()
a = x.list_transfer
get_sorted_transfers(a)
m = x.get_last_info(a)
s = x.code_check(a)
s_1 = x.code_check(a)
print(s)
print(m)
