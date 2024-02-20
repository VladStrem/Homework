import requests
import os
import json


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"


class BankAccount:
    accounts = []
    __exchange_rate = {}

    DATA_FOLDER = 'data'

    @classmethod
    def create_exchange_rate(cls):
        try:
            response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
            exchange_data = response.json()

            cls.__exchange_rate = {rate['cc']: rate['rate'] for rate in exchange_data}
        except requests.RequestException as e:
            print(f"Failed to fetch exchange rates: {e}")

    def __init__(self, account_number, amount, currency, owner_name):
        self.account_number = account_number
        self.balance = Money(amount, currency)
        self.owner_name = owner_name
        type(self).accounts.append(self)

        self.save_state_to_file()

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}, Owner: {self.owner_name}"

    def save_state_to_file(self):
        if not os.path.exists(self.DATA_FOLDER):
            os.makedirs(self.DATA_FOLDER)

        file_path = os.path.join(self.DATA_FOLDER, f"{self.account_number}.txt")

        account_data = {
            'account_number': self.account_number,
            'balance': {
                'amount': self.balance.amount,
                'currency': self.balance.currency,
            },
            'owner_name': self.owner_name,
        }

        with open(file_path, mode='w') as file:
            json.dump(account_data, file, indent=2)

    def delete_account(self):
        type(self).accounts = [account for account in type(self).accounts if account.account_number != self.account_number]
        file_path = os.path.join(self.DATA_FOLDER, f"{self.account_number}.txt")
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Account {self.account_number} deleted along with its file.")
        else:
            print(f"Account {self.account_number} does not have a corresponding file.")

    def deposit(self, amount, currency):
        """Додавання грошей на рахунок."""
        if amount > 0 and currency == self.balance.currency:
            self.balance.amount += amount
            print(f"Deposited {amount} {currency}. New balance: {self.balance}")
            self.save_state_to_file()
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount, currency):
        """Зняття грошей з рахунку."""
        if 0 < amount <= self.balance.amount and currency == self.balance.currency:
            self.balance.amount -= amount
            print(f"Withdrew {amount} {currency}. New balance: {self.balance}")
            self.save_state_to_file()
        elif amount > self.balance.amount:
            print("Insufficient funds. Withdrawal not possible.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def transfer_funds(self, target_account, amount):
        """Переказ коштів на рахунок іншого об'єкта."""
        if amount <= 0:
            print("Invalid transfer amount.")
            return
        source_currency = self.balance.currency
        target_currency = target_account.balance.currency

        print(f"Exchange rates: {self.__exchange_rate}")

        if source_currency != target_currency and source_currency in self.__exchange_rate and target_currency in self.__exchange_rate:
            # Convert the amount to a common currency (e.g, UAH) using exchange rates
            common_currency_amount = amount * self.__exchange_rate[source_currency]
            # Convert the common currency amount to the target currency
            converted_amount = common_currency_amount / self.__exchange_rate[target_currency]
            converted_amount = round(converted_amount, 2)

            if amount <= self.balance.amount:
                self.balance.amount -= amount
                target_account.balance.amount += converted_amount
                print(f"Transferred {amount} {source_currency} to {target_account.owner_name}'s account "
                      f"({converted_amount} {target_currency} credited).")
                self.save_state_to_file()
                target_account.save_state_to_file()
            else:
                print("Insufficient funds. Transfer not possible.")
        elif source_currency == target_currency:
            if amount <= self.balance.amount:
                self.balance.amount -= amount
                target_account.balance.amount += amount
                print(f"Transferred {amount} {source_currency} to {target_account.owner_name}'s account.")
                self.save_state_to_file()
                target_account.save_state_to_file()
            else:
                print("Insufficient funds. Transfer not possible.")
        else:
            print("Currency conversion not possible. Source or target currency not found in exchange rates.")

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        """Класовий метод для пошуку рахунків за власником."""
        matching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                matching_accounts.append(account)
        return matching_accounts


BankAccount.create_exchange_rate()
if __name__  == "__main__":
    account1 = BankAccount("12345", 1000.0, "USD", "John Doe")
    account2 = BankAccount("67890", 2000.0, "EUR", "Alice Smith")

    print(account1)
    print(account2)

    account1.deposit(500.0, "USD")
    account2.withdraw(300.0, "EUR")

    account1.transfer_funds(account2, 200.0)
    account1.transfer_funds(account2, 800.0)
    account1.transfer_funds(account2, 300.0)
    print(account1)
    print(account2)