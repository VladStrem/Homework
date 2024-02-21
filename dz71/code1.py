from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class SalesReport(ABC):
    @abstractmethod
    def generate_report(self):
        pass


class OrderFood(Order):
    def process_order(self):
        print("Processing food order")


class OrderDrink(Order):
    def process_order(self):
        print("Processing drink order")


class PaymentCash(Payment):
    def process_payment(self):
        print("Processing cash payment")


class PaymentCard(Payment):
    def process_payment(self):
        print("Processing card payment")


class SalesReportJSON(SalesReport):
    def generate_report(self):
        print("Generating JSON sales report")


class SalesReportCSV(SalesReport):
    def generate_report(self):
        print("Generating CSV sales report")


class AbstractFactory(ABC):
    @abstractmethod
    def create_order(self):
        pass

    @abstractmethod
    def create_payment(self):
        pass

    @abstractmethod
    def create_sales_report(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_order(self):
        return OrderFood()

    def create_payment(self):
        return PaymentCash()

    def create_sales_report(self):
        return SalesReportJSON()


class ConcreteFactory2(AbstractFactory):
    def create_order(self):
        return OrderDrink()

    def create_payment(self):
        return PaymentCard()

    def create_sales_report(self):
        return SalesReportCSV()


class RestaurantSystem:
    def __init__(self, factory):
        self.order = factory.create_order()
        self.payment = factory.create_payment()
        self.sales_report = factory.create_sales_report()

    def place_order(self):
        self.order.process_order()

    def process_payment(self):
        self.payment.process_payment()

    def generate_sales_report(self):
        self.sales_report.generate_report()


if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    system1 = RestaurantSystem(factory1)

    system1.place_order()
    system1.process_payment()
    system1.generate_sales_report()

    factory2 = ConcreteFactory2()
    system2 = RestaurantSystem(factory2)

    system2.place_order()
    system2.process_payment()
    system2.generate_sales_report()
