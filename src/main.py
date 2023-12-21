import time
from timeit import timeit

from src.Transfer import Transfer


class main:
    transfers = Transfer()
    transfers.get_list_transfer()
    transfers.get_true_sort_transfers()
    transfers.code_check()

    print(transfers.get_count_transfers())
    print(transfers.get_last_info())


if __name__ == '__main__':
    main()
