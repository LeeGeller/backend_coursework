from datetime import datetime
import os
import json


def get_last_transfer():
    with open(os.path.join('..', 'data', 'operations.json'), 'r', encoding='UTF-8') as list_data:
        return json.loads(list_data.read().strip())


print(get_last_transfer())
