def test_get_list_transfer(fixture_list, get_fixture_list):
    assert len(get_fixture_list) != 0
    assert get_fixture_list is not None
    assert get_fixture_list == fixture_list
    assert len(get_fixture_list) == len(fixture_list)


def test_get_true_sort_transfers(get_fixture_transfers_class, fixture_test_list, sorted_list):
    assert get_fixture_transfers_class.get_true_sort_transfers(fixture_test_list) == sorted_list


def test_code_check(fixture_test_list, get_fixture_transfers_class, get_fixture_code_info):
    get_fixture_transfers_class.code_check(fixture_test_list)
    assert get_fixture_transfers_class.list_transfer == get_fixture_code_info


def test_get_last_info(fixture_test_list, get_fixture_transfers_class, get_fixture_list_info):
    get_fixture_transfers_class.get_true_sort_transfers(fixture_test_list)
    get_fixture_transfers_class.code_check(get_fixture_transfers_class.list_transfer)
    get_fixture_transfers_class.get_last_info(fixture_test_list)

    assert get_fixture_transfers_class.last_info == get_fixture_list_info
    assert len(get_fixture_transfers_class.last_info) == len(get_fixture_list_info)
    assert len(get_fixture_transfers_class.last_info) is not None
    assert len(get_fixture_transfers_class.last_info) < len(get_fixture_list_info) * 2
