import datetime

import pytest

from utils.Transfer import Transfer


@pytest.fixture
def get_fixture_list():
    transfers = Transfer()
    transfers.get_list_transfer()
    return transfers.list_transfer


@pytest.fixture
def get_fixture_transfers_class():
    transfers = Transfer()
    return transfers


@pytest.fixture
def fixture_test_list():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]


@pytest.fixture
def sorted_list():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': datetime.datetime(2019, 8, 26, 0, 0),
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': datetime.datetime(2019, 7, 3, 0, 0),
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': datetime.datetime(2018, 6, 30, 0, 0),
             'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
             'to': 'Счет 11776614605963066702'},
            {'id': 587085106, 'state': 'EXECUTED', 'date': datetime.datetime(2018, 3, 23, 0, 0),
             'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]


@pytest.fixture
def get_fixture_code_info():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596 83** ****5199', 'to': 'Счет **9589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158 30** ****6758', 'to': 'Счет **5560'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
             'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Счет 7510 68** ****57916952', 'to': 'Счет **6702'},
            {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
             'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]


@pytest.fixture
def get_fixture_list_info():
    return ('26.08.2019 Перевод организации\n'
            'Maestro 1596 83** ****5199 -> Счет **9589\n'
            '31957.58 руб.\n'
            '\n'
            '03.07.2019 Перевод организации\n'
            'MasterCard 7158 30** ****6758 -> Счет **5560\n'
            '8221.37 USD\n'
            '\n'
            '30.06.2018 Перевод организации\n'
            'Счет 7510 68** ****57916952 -> Счет **6702\n'
            '9824.07 USD\n')
