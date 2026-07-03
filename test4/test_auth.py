import unittest
from .auth import verify_api_token

class TestAuth(unittest.TestCase):

    def test_correct_token(self):
        self.assertTrue(verify_api_token("SUPER_SECRET_TOKEN_123"))

    def test_incorrect_token(self):
        self.assertFalse(verify_api_token("WRONG_TOKEN"))

    def test_wrong_length(self):
        self.assertFalse(verify_api_token("SHORT"))

if __name__ == "__main__":
    unittest.main()
