import time
from datetime import datetime as date
import os
import json


class Transfer:
    def __init__(self):
        self.list_transfer = []
        self.last_info = []
        self.count_transfers = 5

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
        """
        Sort transfer's list
        :return: sorted list
        """
        new_list = []
        for date_ in self.list_transfer:
            str_date = date_.get('date')
            if str_date is not None and date_.get('state') == 'EXECUTED':
                cl_date = date.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
                date_short = cl_date.strftime("%d.%m.%Y")
                date_class = date.strptime(date_short, "%d.%m.%Y")
                date_['date'] = date_class
                new_list.append(date_)

        self.list_transfer = sorted(new_list, key=lambda x: x['date'], reverse=True)
        return self.list_transfer

    def code_check(self):
        """
        Code information about from transfer
        :return: coded info about from
        """
        for i in range(len(self.list_transfer) - 1):
            if self.list_transfer[i].get('from'):
                # Get str about date
                str_info_from, str_info_to = self.list_transfer[i].get('from'), self.list_transfer[i].get('to')
                list_info_from, list_info_to = str_info_from.split(), str_info_to.split()

                # Get number and name card from
                card_info_from = [info for info in list_info_from if info.isdigit()]
                card_from = [info for info in list_info_from if info.isalpha()]

                # Get number and name card to
                card_info_to = [info for info in list_info_to if info.isdigit()]
                card_to = [info for info in list_info_to if info.isalpha()]

                # Join and code str info from
                card_info_from, card_from = ''.join(card_info_from), ' '.join(card_from)
                code_formatted = f'{card_from} {card_info_from[:4]} {card_info_from[4:6]}** ****{card_info_from[12:]}'
                self.list_transfer[i]['from'] = code_formatted

                # Join and code str info to
                card_info_to, card_to = ' '.join(card_to), ''.join(card_info_to)
                code_formatted = f'{card_info_to} **{card_to[len(card_to) - 4:]}'
                self.list_transfer[i]['to'] = code_formatted

        return self.list_transfer

    def get_count_transfers(self):
        """
        Count transfers
        :return: count transfers
        """
        reckon = input("Input 'yes' if you want to text count of transfers: ").strip().lower()
        if reckon == 'yes':
            while True:
                count_transfers = input("How many transfers do you want to see?\n")
                if count_transfers.isdigit():
                    self.count_transfers = count_transfers
                    return self.count_transfers
                print(f"You need input number. Not words.")

    def get_last_info(self):
        """
        Get info about last transfers
        :return: info
        """
        list_info = []

        for i in range(len(self.list_transfer) - 1):
            if self.list_transfer[i].get('from'):
                date_str = self.list_transfer[i].get('date')

                date_formatted = date_str.strftime("%d.%m.%Y")

                last_info = (f"{date_formatted} {self.list_transfer[i]['description']}\n"
                             f"{self.list_transfer[i]['from']} -> {self.list_transfer[i]['to']}\n"
                             f"{self.list_transfer[i]['operationAmount']['amount']} {self.list_transfer[i]['operationAmount']['currency']['name']}\n")
                list_info.append(last_info)
                if len(list_info) > int(self.count_transfers) - 1:
                    break

        self.last_info = '\n'.join(list_info)
        return self.last_info
