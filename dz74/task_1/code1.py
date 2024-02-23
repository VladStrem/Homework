from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def get_price(self) -> float:
        pass


class Product(Component):

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price


class Category(Component):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, child: Component) -> None:
        self.children.append(child)

    def remove_child(self, child: Component) -> None:
        self.children.remove(child)

    def get_children(self):
        return self.children

    def get_price(self) -> float:
        total_price = 0
        for child in self.children:
            total_component = child.get_price()
            total_price += total_component
        return total_price


class Store(Category):
    pass


if __name__ == "__main__":
    store = Store("IFranko")
    catalog1 = Category('box1')
    catalog2 = Category('box2')
    catalog3 = Category('box3')
    catalog4 = Category('box4')
    catalog5 = Category('box5')
    p1 = Product("Apple TV", 100)
    p2 = Product("Samsung A14", 100)
    p3 = Product("Iphone 11 Pro", 100)
    p4 = Product("Iphone XR", 100)
    p5 = Product("Acer Nitro", 200)
    store.add_child(catalog1)
    catalog1.add_child(p1)
    catalog1.add_child(catalog2)
    catalog2.add_child(p2)
    catalog2.add_child(catalog3)
    catalog2.add_child(p3)
    catalog3.add_child(p4)
    catalog3.add_child(catalog4)
    catalog4.add_child(p5)

    print(f"Загальна ціна товарів у магазині: {store.get_price()}")
