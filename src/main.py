from utils.Transfer import Transfer


class main:
    transfers = Transfer()
    list_transfers = transfers.get_list_transfer()
    transfers.get_true_sort_transfers(list_transfers)
    transfers.code_check(list_transfers)

    print(transfers.get_last_info(list_transfers))


if __name__ == '__main__':
    main()
