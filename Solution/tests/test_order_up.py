import builtins
import unittest
from unittest.mock import patch
import order_up


class TestOrderUp(unittest.TestCase):
    def test_get_order_one_item(self):
        order = ["fries"]

        result = order_up.get_order(order)

        self.assertEqual(order, result)

    def test_get_order_duplicate_in_list(self):
        order = ["fries", "fries", "fries", "burger"]

        result = order_up.get_order(order)

        self.assertEqual(order, result)

    def test_get_order_not_on_menu(self):
        order = ["banana", "cereal", "cookie"]
        expected_result = ["cookie"]

        result = order_up.get_order(order)

        self.assertEqual(expected_result, result)

    @patch("builtins.input", return_value="yes")
    def test_is_order_complete_yes(self, input_patch):
        self.assertEqual(builtins.input, input_patch)

        result = order_up.is_order_complete()

        self.assertFalse(result)

    @patch("builtins.input", side_effect=["banana", "cookie", "yes", "fries", "no"])
    def test_get_order_valid(self, input_patch):
        self.assertEqual(builtins.input, input_patch)
        expected_result = ["cookie", "fries"]

        result = order_up.get_order()

        self.assertEqual(expected_result, result)
