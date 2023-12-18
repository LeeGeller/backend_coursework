import unittest
from utils.get_list_transfer import Transfer

class TestTransferInfo(unittest.TestCase):
    def test_get_list_transfer_above_zero(self):
        self.assertNotEqual(Transfer().get_last_transfer(), 0)
        self.assertNotEqual(Transfer().get_last_transfer(), None)
