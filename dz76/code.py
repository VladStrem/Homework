from abc import ABC, abstractmethod


class Ingredient(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass


class Mayo(Ingredient):
    def get_price(self) -> float:
        return 1.0


class Mustard(Ingredient):
    def get_price(self) -> float:
        return 0.8


class Ketchup(Ingredient):
    def get_price(self) -> float:
        return 1.2


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.get_price() for item in self.items)


class HotDog(ABC):
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    @abstractmethod
    def get_price(self):
        pass


class StandardHotDog(HotDog):
    def get_price(self):
        return 3.0 + sum(ingredient.get_price() for ingredient in self.ingredients)


class Discount:
    @abstractmethod
    def apply_discount(self, total_price):
        pass


class ThreeHotDogsDiscount(Discount):
    def apply_discount(self, total_price):
        if total_price >= 9.0:
            return total_price * 0.9
        return total_price


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Paid {amount} in cash")


class CardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Paid {amount} with a card")


class SalesReport:
    @abstractmethod
    def generate_report(self, orders):
        pass


class SimpleSalesReport(SalesReport):
    def generate_report(self, orders):
        total_sold = len(orders)
        total_revenue = sum(order.calculate_total() for order in orders)
        print(f"Total Hot Dogs Sold: {total_sold}")
        print(f"Total Revenue: {total_revenue}")


class IngredientInventory:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, ingredient, quantity):
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity

    def display_inventory(self):
        print("Ingredient Inventory:")
        for ingredient, quantity in self.ingredients.items():
            print(f"{ingredient.__class__.__name__}: {quantity}")


class HotDogKiosk:
    def __init__(self):
        self.order_history = []
        self.discount_strategy = ThreeHotDogsDiscount()
        self.payment_method = CardPayment()
        self.sales_report = SimpleSalesReport()
        self.ingredient_inventory = IngredientInventory()

    def create_hot_dog(self, hot_dog_type):
        return hot_dog_type("Standard")

    def take_order(self, hot_dog, ingredients):
        order = Order()
        order.add_item(hot_dog)
        for ingredient in ingredients:
            order.add_item(ingredient)
            self.ingredient_inventory.add_ingredient(ingredient, 1)
        self.order_history.append(order)
        return order

    def process_payment(self, order):
        total_price = order.calculate_total()
        discounted_price = self.discount_strategy.apply_discount(total_price)
        self.payment_method.process_payment(discounted_price)

    def display_sales_report(self):
        self.sales_report.generate_report(self.order_history)

    def display_ingredient_inventory(self):
        self.ingredient_inventory.display_inventory()


kiosk = HotDogKiosk()

standard_hot_dog = kiosk.create_hot_dog(StandardHotDog)

mayo = Mayo()
mustard = Mustard()
ketchup = Ketchup()

order1 = kiosk.take_order(standard_hot_dog, [mayo, ketchup])

kiosk.process_payment(order1)

kiosk.display_sales_report()
kiosk.display_ingredient_inventory()
