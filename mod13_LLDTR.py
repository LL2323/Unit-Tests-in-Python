import unittest
import re
from datetime import datetime


class StockVisualizerInputTests(unittest.TestCase):

    def test_symbol(self):
        self.assertIsNotNone(re.fullmatch(r"[A-Z]{1,7}", "AAPL"))
        self.assertIsNone(re.fullmatch(r"[A-Z]{1,7}", "aapl"))
        self.assertIsNone(re.fullmatch(r"[A-Z]{1,7}", "AAPL1"))
        self.assertIsNone(re.fullmatch(r"[A-Z]{1,7}", "TOOLONGSYMBOL"))

    def test_chart_type(self):
        self.assertIn("1", ["1", "2"])
        self.assertIn("2", ["1", "2"])
        self.assertNotIn("3", ["1", "2"])

    def test_time_series(self):
        choices = ["1", "2", "3", "4"]
        self.assertIn("1", choices)
        self.assertIn("4", choices)
        self.assertNotIn("5", choices)

    def test_start_date(self):
        date = "2024-02-29"
        self.assertIsNotNone(re.fullmatch(r"\d{4}-\d{2}-\d{2}", date))
        datetime.strptime(date, "%Y-%m-%d")

        invalid_date = "2023-02-29"
        with self.assertRaises(ValueError):
            datetime.strptime(invalid_date, "%Y-%m-%d")

    def test_end_date(self):
        date = "2024-12-31"
        self.assertIsNotNone(re.fullmatch(r"\d{4}-\d{2}-\d{2}", date))
        datetime.strptime(date, "%Y-%m-%d")

        invalid_date = "12-31-2024"
        self.assertIsNone(re.fullmatch(r"\d{4}-\d{2}-\d{2}", invalid_date))
