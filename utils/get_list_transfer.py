from datetime import datetime as date
import os
import json
from operator import itemgetter


class Transfer:
    def __init__(self):
        self.list_transfer = []
        self.last_info = {}

    def __repr__(self):
        return (f"Return file with informstion\n"
                f"about user:\n"
                f"{self.list_transfer}\n"
                f"Return 5 last transfers:\n"
                f"{self.last_info}")

    def get_list_transfer(self):
        with open(os.path.join('..', 'data', 'operations.json'), 'r', encoding='UTF-8') as list_data:
            self.list_transfer = json.loads(list_data.read().strip())
        return self.list_transfer

    def get_last_five_transfers(self):
        current_transfer = []
        list_transfers = self.list_transfer
        count = 5
        while count > 0:
            for i in range(len(self.list_transfer) - 1):
                max_date = date.now()
                next_date = list_transfers[i + 1].get('date')

                if next_date:
                    if list_transfers[i].get('state') == 'EXECUTED':
                        first_date = list_transfers[i].get('date')
                        date_1 = date.strptime(first_date, '%Y-%m-%dT%H:%M:%S.%f')
                        date_2 = date.strptime(next_date, '%Y-%m-%dT%H:%M:%S.%f')
                        if date_1 > date_2:
                            max_date = date_1
                            count -= 1

                current_transfer.append(list_transfers[i])
                self.last_info = current_transfer
            return self.last_info


x = Transfer()
x.get_list_transfer()
x.get_last_five_transfers()

print(x)
