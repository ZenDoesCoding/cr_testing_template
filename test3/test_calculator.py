import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculator import add_to_total

class TestCalculator(unittest.TestCase):

    def test_add_to_total(self):
        result = add_to_total(5)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
