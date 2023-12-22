import datetime
import json
import pathlib

import pytest

from utils.Transfer import Transfer


@pytest.fixture
def get_fixture_transfers_class():
    transfers = Transfer()
    return transfers


@pytest.fixture
def test_data_file():
    with open(pathlib.Path('test_data.json')) as file:
        return json.loads(file.read())


@pytest.fixture
def test_data_sort(test_data_file):
    new_list = []
    for value in test_data_file:
        if value.get('state') == 'EXECUTED' and value.get('from'):
            new_list.append(value)
        else:
            continue

    new_list = sorted(new_list, key=lambda x: x.get('date'), reverse=True)
    test_data_file = new_list[:5]

    return test_data_file


@pytest.fixture
def test_sort_list():
    return [{'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
             'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
             'to': 'Счет 35158586384610753655'},
            {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
             'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
             'to': 'Счет 43241152692663622869'},
            {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
             'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
             'to': 'Счет 46765464282437878125'},
            {'id': 509645757, 'state': 'EXECUTED', 'date': '2019-10-30T01:49:52.939296',
             'operationAmount': {'amount': '23036.03', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод с карты на счет', 'from': 'Visa Gold 7756673469642839',
             'to': 'Счет 48943806953649539453'},
            {'id': 888407131, 'state': 'EXECUTED', 'date': '2019-09-29T14:25:28.588059',
             'operationAmount': {'amount': '45849.53', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 35421428450077339637',
             'to': 'Счет 46723050671868944961'}]


@pytest.fixture
def test_info_code():
    return [{'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
             'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Visa Classic 2842 87** ****9012', 'to': 'Счет **3655'},
            {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
             'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 7810 84** ****5568', 'to': 'Счет **2869'},
            {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
             'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 3861 14** ****55669794', 'to': 'Счет **8125'},
            {'id': 509645757, 'state': 'EXECUTED', 'date': '2019-10-30T01:49:52.939296',
             'operationAmount': {'amount': '23036.03', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод с карты на счет', 'from': 'Visa Gold 7756 67** ****2839', 'to': 'Счет **9453'},
            {'id': 888407131, 'state': 'EXECUTED', 'date': '2019-09-29T14:25:28.588059',
             'operationAmount': {'amount': '45849.53', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 3542 14** ****77339637', 'to': 'Счет **4961'}]


@pytest.fixture
def test_last_info_data():
    return ('07.12.2019 Перевод организации\n'
            'Visa Classic 2842878893689012 -> Счет 35158586384610753655\n'
            '48150.39 USD\n'
            '\n'
            '19.11.2019 Перевод организации\n'
            'Maestro 7810846596785568 -> Счет 43241152692663622869\n'
            '30153.72 руб.\n'
            '\n'
            '13.11.2019 Перевод со счета на счет\n'
            'Счет 38611439522855669794 -> Счет 46765464282437878125\n'
            '62814.53 руб.\n'
            '\n'
            '30.10.2019 Перевод с карты на счет\n'
            'Visa Gold 7756673469642839 -> Счет 48943806953649539453\n'
            '23036.03 руб.\n'
            '\n'
            '29.09.2019 Перевод со счета на счет\n'
            'Счет 35421428450077339637 -> Счет 46723050671868944961\n'
            '45849.53 USD\n')
