from datetime import datetime as date


def get_sorted_transfers(transfers_list):
    if len(transfers_list) <= 1:
        return transfers_list
    else:
        left_list = []
        right_list = []

        for i in range(len(transfers_list) - 1):
            date_next = transfers_list[i + 1].get('date')
            if date_next:
                date_next_formatted = date.strptime(date_next, '%Y-%m-%dT%H:%M:%S.%f')
                if transfers_list[i].get('state') == 'EXECUTED':
                    first_date = transfers_list[i].get('date')
                    date_1 = date.strptime(first_date, '%Y-%m-%dT%H:%M:%S.%f')
                    if date_1 >= date_next_formatted:
                        left_list.append(transfers_list[i])
                    else:
                        right_list.append(transfers_list[i])
                return get_sorted_transfers(left_list)
