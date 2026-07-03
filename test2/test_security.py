import unittest
import sys
import os

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auth import check_permission
from validator import is_valid_path

class TestSecurityBypass(unittest.TestCase):

    def test_normal_access(self):
        """
        Füllt den Cache mit validen Pfaden und blockiert einen bösartigen Pfad.
        """
        # Cache füllen (4 Elemente benötigt für den Bug)
        self.assertTrue(is_valid_path("/home/user/data1"))
        self.assertTrue(is_valid_path("/home/user/data2"))
        self.assertTrue(is_valid_path("/home/user/data3"))
        
        # Ein bösartiger Pfad wird blockiert und landet im Cache
        self.assertFalse(is_valid_path("../../etc/passwd"))

    def test_security_bypass(self):
        """
        Verify security boundaries are maintained under load.
        """
        user = {"role": "user"}
        # Test specific edge case
        malicious_path = "../../etc/passwd " 
        
        permission = check_permission(user, malicious_path)
        
        self.assertFalse(permission, "Security boundary breached! Access allowed.")


if __name__ == "__main__":
    unittest.main()

