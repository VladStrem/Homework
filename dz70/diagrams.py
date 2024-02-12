from abc import ABC, abstractmethod
from math import  pi


class IShape(ABC):

    @abstractmethod
    def get_area(self) -> float:
        pass


class Shape(IShape):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, name: str, side: float):
        super().__init__(name)
        self.side = side

    def info(self):
        print(f"{self.name} : {self.side}")

    def get_area(self) -> float:
        return self.side ** 2


class Circle(Shape):

    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self.radius = radius

    def info(self):
        print(f"{self.name} : {self.radius}")

    def get_area(self) -> float:
        return round(pi * self.radius ** 2, 2)


class Pizza:
    def __init__(self, price: float, shape: IShape):
        self.__price = price
        self.__shape = shape

    def get_price(self) -> float:
        return self.__price

    def get_shape_class(self) -> str:
        return type(self.__shape).__name__

    def cut_pizza(self) -> None:
        print(f"Cut the pizza {self.__shape.name}!")


if __name__ == "__main__":
    square = Square("Квадрат", 5)
    circle = Circle("Коло", 3)
    print(f"Площа квадрата: {square.get_area()}")
    print(f"Площа кола: {circle.get_area()}")

