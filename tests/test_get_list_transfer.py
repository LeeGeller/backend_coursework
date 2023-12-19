import unittest
from utils.Transfer import Transfer
from utils.get_sorted_transfers import get_sorted_transfers


class TestTransferInfo(unittest.TestCase):
    def test_get_list_transfer_above_zero(self):
        self.assertNotEqual(Transfer().get_list_transfer(), 0)
        self.assertNotEqual(Transfer().get_list_transfer(), None)

    def test_get_last_five_transfers(self):
        self.assertNotEqual(get_sorted_transfers(Transfer().get_list_transfer()), Transfer().get_list_transfer())

    # def test_get_last_five_transfers_count(self):
    #     self.assertEqual(len(Transfer().last_info), 5)
