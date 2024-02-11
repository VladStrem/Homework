from newbankaccount import NewBankAccount


class UpBankAccount(NewBankAccount):
    def __init__(self, account_number, amount, currency, owner_name, max_limit, max_count_transactions):
        super().__init__(account_number, amount, currency, owner_name, max_limit, max_count_transactions)
        self.transaction_count = 0

    def __bool__(self):
        """Override the bool operator to check if the balance is positive."""
        return self.balance.amount > 0

    def __float__(self):
        """Override the float operator to return the float representation of the balance."""
        return float(self.balance.amount)

    def __lt__(self, other):
        """Override the less than operator to compare account balances in UAH."""
        if self.balance.currency != other.balance.currency:
            self_balance_uah = self.convert_to_uah()
            other_balance_uah = other.convert_to_uah()
            return self_balance_uah < other_balance_uah
        else:
            return self.balance.amount < other.balance.amount

    def __eq__(self, other):
        """Override the equality operator to compare currencies and amounts."""
        return self.balance.currency == other.balance.currency and self.balance.amount == other.balance.amount

    def __add__(self, numb):
        """Override the addition operator to deposit funds into the account."""
        if numb > 0:
            self.deposit(numb, self.balance.currency)
        else:
            print("Invalid deposit amount. Please enter a positive number.")
        return self

    def __sub__(self, numb):
        """Override the subtraction operator to withdraw funds from the account."""
        if numb > 0:
            self.withdraw(numb, self.balance.currency)
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")
        return self

    def __call__(self, value=0):
        """Override the call method to perform actions based on the provided value."""
        if value < 0:
            self.withdraw(abs(value), self.balance.currency)
            print(f"Withdrawal of {abs(value)} {self.balance.currency}. New balance: {self.balance}")
        elif value > 0:
            self.deposit(value, self.balance.currency)
            print(f"Deposit of {value} {self.balance.currency}. New balance: {self.balance}")
        else:
            print(f"Current balance: {self.balance}")


if __name__ == "__main__":
    account1 = UpBankAccount("12345", 1000.0, "USD", "Alice Smith", max_limit=500.0, max_count_transactions=3)
    account2 = UpBankAccount("67890", -2000.0, "USD", "Bob Johnson", max_limit=1000.0, max_count_transactions=5)

    print("Is account1 positive:", bool(account1))
    print("Is account2 positive:", bool(account2))

    print("Float representation of account1:", float(account1))
    print("Float representation of account2:", float(account2))

    print("Account 1 < Account 2:", account1 < account2)
    print("Account 2 < Account 1:", account2 < account1)

    account1 = account1 + 500.0
    print("After deposit:", account1)
    account1 = account1 - 200.0
    print("After withdrawal:", account1)
    account1(-10)
    account1(20)
    account1()