import pathlib
from datetime import datetime as date
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

    def get_true_sort_transfers(self, list_):
        """
        clean and sort list without artefacts and with tru info
        :param list_: list
        :return: self.list_transfer
        """
        new_list = []
        for value in list_:
            if value.get('state') == 'EXECUTED' and value.get('from'):
                new_list.append(value)
            else:
                continue

        new_list = sorted(new_list, key=lambda x: x.get('date'), reverse=True)
        self.list_transfer = new_list[:5]

        return self.list_transfer

    def code_check(self, list_):
        """
        Code information about from transfer
        :return: self.list_transfer
        """

        for i in list_:
            # Get str about date and split these
            str_info_from, str_info_to = i.get('from'), i.get('to')
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
            i['from'] = code_formatted

            # Join and code str info to
            card_info_to, card_to = ' '.join(card_to), ''.join(card_info_to)
            code_formatted = f'{card_info_to} **{card_to[len(card_to) - 4:]}'
            i['to'] = code_formatted

        self.list_transfer = list_

        return self.list_transfer

    def get_last_info(self, list_):
        """
        Get info about last transfers
        :return: self.last_info
        """
        last_info = []

        for info in list_:
            date_str = info.get('date')
            date_class = date.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
            date_formatted = date_class.strftime("%d.%m.%Y")

            last_ = (f"{date_formatted} {info['description']}\n"
                     f"{info['from']} -> {info['to']}\n"
                     f"{info['operationAmount']['amount']} {info['operationAmount']['currency']['name']}\n")
            last_info.append(last_)

        list_info = '\n'.join(last_info)
        self.last_info = list_info
        return self.last_info
