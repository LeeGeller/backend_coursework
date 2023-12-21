import pathlib

from utils.Transfer import Transfer


class main:
    DATA = pathlib.Path('..', 'data', 'operations.json')
    transfers = Transfer()
    get_list_transfers = transfers.get_list_transfer(DATA)
    transfers.get_true_sort_transfers(transfers.list_transfer)
    transfers.code_check(transfers.list_transfer)

    print(transfers.get_last_info(transfers.list_transfer))


if __name__ == '__main__':
    main()
