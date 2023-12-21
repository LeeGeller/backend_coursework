import unittest
from src.Transfer import Transfer



class TestTransferInfo(unittest.TestCase):
    def test_get_list_transfer_above_zero(self):
        self.assertNotEqual(Transfer().get_list_transfer(), 0)
        self.assertNotEqual(Transfer().get_list_transfer(), None)

    def test_get_true_sort_transfers(self):
        transfers_1 = Transfer()
        transfers_1.get_list_transfer()
        transfers_1.get_true_sort_transfers()

        transfers_2 = Transfer()
        transfers_2.get_list_transfer()

        self.assertNotEqual(transfers_1.list_transfer, transfers_2.list_transfer)
