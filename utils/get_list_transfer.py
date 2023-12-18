from datetime import datetime
import os
import json


class Transfer:
    def __init__(self):
        self.list_transfer = []

    def __repr__(self):
        return (f"Return file with informstion\n"
                f"about user:\n"
                f"{self.list_transfer}")

    def get_last_transfer(self):
        with open(os.path.join('..', 'data', 'operations.json'), 'r', encoding='UTF-8') as list_data:
            self.list_transfer = json.loads(list_data.read().strip())
        return self.list_transfer

    def get_five_last_transfer(self):
        pass


x = Transfer()
print(x)
