import pathlib

from utils.Transfer import Transfer
from utils.get_list_transfer import get_list_transfer


class main:
    DATA = pathlib.Path('..', 'data', 'operations.json')
    transfers = Transfer()
    list_transfers = get_list_transfer(DATA)
    transfers.get_true_sort_transfers(list_transfers)
    transfers.code_check(transfers.list_transfer)

    print(transfers.get_last_info(transfers.list_transfer))


if __name__ == '__main__':
    main()
