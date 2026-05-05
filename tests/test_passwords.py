import unittest
from services.password_service import PasswordService

class TestPassword(unittest.TestCase):

    def test_length(self):
        service = PasswordService()
        pwd = service.generate(5)
        self.assertEqual(len(pwd), 5)

    def test_not_empty(self):
        service = PasswordService()
        pwd = service.generate(5)
        self.assertTrue(pwd != "")
        
    def test_zero_length(self):
        service = PasswordService()
        pwd = service.generate(0)
        self.assertEqual(pwd, "")

if __name__ == "__main__":
    unittest.main()
