import unittest
from utils.get_list_transfer import get_last_transfer

class TestTransferInfo(unittest.TestCase):
    def test_get_list_transfer_above_zero(self):
        self.assertNotEqual(get_last_transfer(), 0)
        self.assertNotEqual(get_last_transfer(), None)
