import unittest

from mock import MagicMock

from src.calculator import Calculatora


class MockTestCase(unittest.TestCase):

    def setUp(self):
        pass

    # Get email from db
    def test_get_email_from_result(self):
        m = MagicMock()
        m.get_mail = MagicMock(return_value="asd@asd.com")
        calc = Calculatora(m)
        self.assertEqual(calc.get_mail_from_calculation(2, 1, "+"), "asd@asd.com")

    # Check email not found from db
    def test_mail_not_found(self):
        m = MagicMock()
        m.get_mail = MagicMock(return_value=None)
        calc = Calculatora(m)
        self.assertEqual(calc.get_mail_from_calculation(2, 1, "+"), None)

    # Remove mail form db
    def test_remove_mail(self):
        m = MagicMock()
        m.remove_mail = MagicMock(return_value=True)
        calc = Calculatora(m)
        self.assertEqual(calc.remove_mail_from_calculation(2, 1, "+"), True)

    # Check email not found from db
    def test_remove_not_found_mail(self):
        m = MagicMock()
        m.remove_mail = MagicMock(return_value=None)
        calc = Calculatora(m)
        self.assertEqual(calc.remove_mail_from_calculation(2, 1, "+"), None)

    # Check user not found from db
    def test_remove_not_found_user(self):
        m = MagicMock()
        m.remove_user = MagicMock(return_value=True)
        calc = Calculatora(m)
        self.assertEqual(calc.remove_user_from_calculation(2, 1, "+"), True)

    # Remove user form db
    def test_user_remove(self):
        m = MagicMock()
        m.remove_user = MagicMock(return_value=True)
        calc = Calculatora(m)
        self.assertEqual(calc.remove_user_from_calculation(2, 1, "+"), True)

    # Get user from db
    def test_get_user_from_result(self):
        m = MagicMock()
        m.get_user = MagicMock(return_value="user1")
        calc = Calculatora(m)
        self.assertEqual(calc.get_user_from_calculation(2, 1, "+"), "user1")

    # Check email not found from db
    def test_user_not_found(self):
        m = MagicMock()
        m.get_user = MagicMock(return_value=None)
        calc = Calculatora(m)
        self.assertEqual(calc.get_user_from_calculation(2, 1, "+"), None)

if __name__ == '__main__':
    unittest.main()
