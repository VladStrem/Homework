import unittest
from BankAccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        BankAccount.create_exchange_rate()
        self.account1 = BankAccount("12345", 1000.0, "USD", "John Doe")
        self.account2 = BankAccount("67890", 2000.0, "EUR", "Alice Smith")

    def test_deposit(self):
        self.account1.deposit(500.0, "USD")
        self.assertEqual(self.account1.balance.amount, 1500.0)

    def test_withdraw(self):
        self.account2.withdraw(300.0, "EUR")
        self.assertEqual(self.account2.balance.amount, 1700.0)

    def test_transfer_funds(self):
        self.account1.transfer_funds(self.account2, 200.0)
        self.assertEqual(self.account1.balance.amount, 800.0)

    def test_find_accounts_by_owner(self):
        matching_accounts = BankAccount.find_accounts_by_owner("John Doe")
        self.assertIn(self.account1, matching_accounts)
        self.assertNotIn(self.account2, matching_accounts)
