from datetime import datetime as date
import os
import json


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
        """
        :return: get operations.json
        """
        with open(os.path.join('..', 'data', 'operations.json'), 'r', encoding='UTF-8') as list_data:
            self.list_transfer = json.loads(list_data.read().strip())
        return self.list_transfer

    def get_true_sort_transfers(self):
        new_list = []
        for date_ in self.list_transfer:
            str_date = date_.get('date')
            if str_date is not None:
                cl_date = date.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
                date_short = cl_date.strftime("%d.%m.%Y")
                date_class = date.strptime(date_short, "%d.%m.%Y")
                date_['date'] = date_class
                new_list.append(date_)

        self.list_transfer = sorted(new_list, key=lambda x: x['date'], reverse=True)
        return self.list_transfer

    def code_check_from(self):
        for i in range(len(self.list_transfer) - 1):
            if self.list_transfer[i].get('from'):
                str_info = self.list_transfer[i].get('from')
                list_info = str_info.split()
                card_info = [info for info in list_info if info.isdigit()]
                card = [info for info in list_info if info.isalpha()]
                card_info = ''.join(card_info)
                card = ' '.join(card)
                code_formatted = f'{card} {card_info[:4]} {card_info[4:6]}** ****{card_info[12:]}'
                self.list_transfer[i]['from'] = code_formatted

        return self.list_transfer

    def code_check_to(self):
        for i in range(len(self.list_transfer) - 1):
            if self.list_transfer[i].get('to'):
                str_info = self.list_transfer[i].get('to')
                list_info = str_info.split()
                number = list_info[1]
                code_formatted = f'Счет **{number[16:]}'
                self.list_transfer[i]['to'] = code_formatted
        return self.list_transfer

    def get_last_info(self):
        list_info = []

        for i in range(len(self.list_transfer) - 1):
            if self.list_transfer[i].get('from'):
                date_str = self.list_transfer[i].get('date')

                date_formatted = date_str.strftime("%d.%m.%Y")

                last_info = (f"{date_formatted} {self.list_transfer[i]['description']}\n"
                             f"{self.list_transfer[i]['from']} -> {self.list_transfer[i]['to']}\n"
                             f"{self.list_transfer[i]['operationAmount']['amount']} {self.list_transfer[i]['operationAmount']['currency']['name']}\n")
                list_info.append(last_info)
                if len(list_info) > 4:
                    break

        self.last_info = '\n'.join(list_info)
        return self.last_info

x = Transfer()
x.get_list_transfer()
x.get_true_sort_transfers()
x.code_check_from()
x.code_check_to()

print(x.list_transfer)
print(x.get_last_info())