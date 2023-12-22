import json


def get_list_transfer(data_path):
    """
    :return: get operations.json
    """

    with open(data_path, 'r', encoding='UTF-8') as list_data:
        list_transfer = json.loads(list_data.read().strip())
    return list_transfer
