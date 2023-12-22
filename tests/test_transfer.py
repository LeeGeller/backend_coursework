import pathlib

from utils.Transfer import Transfer
from utils.get_list_transfer import get_list_transfer


def test_get_list_transfer(test_data_file):
    assert get_list_transfer('test_data.json') is not None
    assert get_list_transfer('test_data.json') == test_data_file


def test_get_true_sort_transfers(test_data_file, test_sort_list):
    assert Transfer().get_true_sort_transfers(test_data_file) == test_sort_list
    assert Transfer().get_true_sort_transfers(test_data_file) != test_data_file


def test_code_check(test_info_code, test_sort_list):
    assert Transfer().code_check(test_sort_list) == test_info_code
    assert len(Transfer().code_check(test_sort_list)) == len(test_info_code)
    assert type(Transfer().code_check(test_sort_list)) == type(test_info_code)


def test_get_last_info(test_sort_list, test_last_info_data):
    assert Transfer().get_last_info(test_sort_list) == test_last_info_data
    assert len(Transfer().get_last_info(test_sort_list)) == len(test_last_info_data)
