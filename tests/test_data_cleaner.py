import unittest

from data_cleaner import clean_csv

CSV = "name,age,city\n张三,20,北京\n张三,20,北京\n 李四 ,30, \n王五,,上海\n"


class TestCleaner(unittest.TestCase):
    def test_dedup(self):
        rows, rep = clean_csv(CSV)
        self.assertEqual(len(rows), 3)
        self.assertGreaterEqual(rep["duplicates_removed"], 1)

    def test_trim(self):
        rows, _ = clean_csv(CSV)
        li = [r for r in rows if r["name"] == "李四"][0]
        self.assertEqual(li["name"], "李四")

    def test_missing(self):
        _, rep = clean_csv(CSV)
        self.assertGreaterEqual(rep["missing_cells"], 1)

    def test_columns(self):
        _, rep = clean_csv(CSV)
        self.assertEqual(rep["columns"], ["name", "age", "city"])


if __name__ == "__main__":
    unittest.main()
