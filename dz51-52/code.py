
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"


class BankAccount:
    accounts = []
    __exchange_rate = {}

    @classmethod
    def create_exchange_rate(cls):
        try:
            response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
            exchange_data = response.json()
        except Exception as e:
            print(e)
    def __init__(self, account_number, amount, currency, owner_name):
        self.account_number = account_number
        self.balance = Money(amount, currency)
        self.owner_name = owner_name
        type(self).accounts.append(self)

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}, Owner: {self.owner_name}"

    def deposit(self, amount, currency):
        """Додавання грошей на рахунок."""
        if amount > 0 and currency == self.balance.currency:
            self.balance.amount += amount
            print(f"Deposited {amount} {currency}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount, currency):
        """Зняття грошей з рахунку."""
        if 0 < amount <= self.balance.amount and currency == self.balance.currency:
            self.balance.amount -= amount
            print(f"Withdrew {amount} {currency}. New balance: {self.balance}")
        elif amount > self.balance.amount:
            print("Insufficient funds. Withdrawal not possible.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    # def change_owner_name(self, new_owner_name):
    #     """Зміна імені власника рахунку."""
    #     self.owner_name = new_owner_name
    #     print(f"Owner name changed to {new_owner_name}.")
    #
    # def display_account_info(self):
    #     """Виведення повної інформації про рахунок."""
    #     print(f"Account Information:\n{self}")

    def transfer(self, recipient_account, amount):
        """Переказ коштів на рахунок іншого об'єкта."""
        if amount <= 0 or self.balance.currency != recipient_account.balance.currency:
            print("Invalid transfer amount or currency mismatch.")
            return

        if amount <= self.balance.amount:
            self.balance.amount -= amount
            recipient_account.balance.amount += amount
            print(f"Transferred {amount} {self.balance.currency} to {recipient_account.owner_name}'s account.")
        else:
            print("Insufficient funds. Transfer not possible.")

    # @staticmethod
    # def check_account_number(account_number):
    #     """Статичний метод для перевірки валідності номера рахунку."""
    #     return isinstance(account_number, str) and len(account_number) == 5 and account_number.isdigit()
    #
    # @property
    # def account_number(self):
    #     """Getter method using @property decorator."""
    #     return self.__account_number
    #
    # @account_number.setter
    # def account_number(self, new_account_number):
    #     """Setter method using @account_number.setter decorator."""
    #     if not self.check_account_number(new_account_number):
    #         raise ValueError("Invalid account number. Please provide a valid 5-digit account number.")
    #     for account in BankAccount.accounts:
    #         if account.__account_number == new_account_number:
    #             raise ValueError("Account with this account number already exists.")
    #     self.__account_number = new_account_number
    #     print(f"Account number changed to {new_account_number}.")

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        """Класовий метод для пошуку рахунків за власником."""
        matching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                matching_accounts.append(account)
        return matching_accounts

    # @classmethod
    # def get_average_balance(cls):
    #     """Класовий метод для отримання середнього балансу усіх об'єктів BankAccount."""
    #     if not cls.accounts:
    #         return 0.0
    #     total_balance = sum(account._balance for account in cls.accounts)
    #     return round(total_balance / len(cls.accounts), 2)


account1 = BankAccount("12345", 1000.0, "USD", "John Doe")
account2 = BankAccount("67890", 2000.0, "USD", "Alice Smith")

print(account1)
print(account2)

# Test deposit, withdraw, and transfer methods
account1.deposit(500.0, "USD")
account2.withdraw(300.0, "USD")

account1.transfer(account2, 200.0)  # Valid transfer between accounts with the same currency
account1.transfer(account2, 800.0)  # Invalid transfer due to insufficient funds
account1.transfer(account2, 300.0)  # Invalid transfer due to currency mismatch
print(account1)
print(account2)
# Test finding accounts by owner
accounts_for_john = BankAccount.find_accounts_by_owner("John Doe")
print(f"Accounts for John Doe: {accounts_for_john}")