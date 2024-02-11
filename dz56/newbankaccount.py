from BankAccount import BankAccount


class NewBankAccount(BankAccount):
    def __init__(self, account_number, amount, currency, owner_name, max_limit, max_count_transactions):
        super().__init__(account_number, amount, currency, owner_name)

        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions
        self.transaction_count = 0

    def withdraw(self, amount, currency):
        # Check if the withdrawal exceeds the maximum limit and count of transactions
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.max_limit:
            print(f"Withdrawal amount exceeds the maximum limit of {self.max_limit} {currency}.")
        elif self.transaction_count >= self.max_count_transactions:
            print(f"Maximum number of transactions ({self.max_count_transactions}) reached. Withdrawal not allowed.")
        else:
            # Call the withdraw method of the parent class
            super().withdraw(amount, currency)
            # Increment the transaction count
            self.transaction_count += 1

    def transfer_funds(self, target_account, amount):
        # Check if the transfer amount exceeds the maximum limit and count of transactions
        if amount <= 0:
            print("Invalid transfer amount.")
        elif amount > self.max_limit:
            print(f"Transfer amount exceeds the maximum limit of {self.max_limit} {self.balance.currency}.")
        elif self.transaction_count >= self.max_count_transactions:
            print(f"Maximum number of transactions ({self.max_count_transactions}) reached. Transfer not allowed.")
        else:
            # Call the transfer_funds method of the parent class
            super().transfer_funds(target_account, amount)
            # Increment the transaction count
            self.transaction_count += 1

    def accrue_interest(self, percentage):
        """Accrue interest on the account balance based on the specified percentage."""
        if percentage < 0:
            print("Invalid interest percentage. Please enter a non-negative value.")
        else:
            interest_amount = self.balance.amount * (percentage / 100)
            self.balance.amount += interest_amount
            print(f"Interest accrued: {interest_amount} {self.balance.currency}. New balance: {self.balance}")


if __name__ == "__main__":
    account4 = NewBankAccount("24680", 5000.0, "USD", "Bob Johnson", max_limit=1000.0, max_count_transactions=5)

    print(account4)
    account4.accrue_interest(10.0)
    print(account4)
    account4.accrue_interest(15)
