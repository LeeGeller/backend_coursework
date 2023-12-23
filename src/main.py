import os
from Transfer import Transfer
from config import DATA


class main:
    transfers = Transfer()
    transfers.get_list_transfer(DATA)
    transfers.get_true_sort_transfers(transfers.list_transfer)
    transfers.code_check(transfers.list_transfer)
    print(os.path.abspath('operations.json'))

    print(transfers.get_last_info(transfers.list_transfer))


if __name__ == '__main__':
    main()
