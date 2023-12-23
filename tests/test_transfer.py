import os.path

from config import DIR_ROOT
from src.Transfer import Transfer


def test_get_list_transfer(fixture_data):
    test_path = os.path.join(DIR_ROOT, 'tests', 'test_data.json')
    real_path = os.path.join(DIR_ROOT, 'data', 'operations.json')
    zero_path = os.path.join(DIR_ROOT, '')

    assert Transfer().get_list_transfer(test_path) == fixture_data
    assert Transfer().get_list_transfer(real_path) == fixture_data
    assert Transfer().get_list_transfer(zero_path) == "No such directory"


def test_get_true_sort_transfers(fixture_data, test_sort_list):
    assert Transfer().get_true_sort_transfers(fixture_data) == test_sort_list


def test_code_check(test_info_code, test_sort_list):
    assert Transfer().code_check(test_sort_list) == test_info_code


def test_get_last_info(test_sort_list, test_last_info_data):
    assert Transfer().get_last_info(test_sort_list) == test_last_info_data
