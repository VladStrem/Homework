from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def fill_color(self, color):
        pass

    @abstractmethod
    def erase(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

    def fill_color(self, color):
        print(f"Filling the circle with {color} color")

    def erase(self):
        print("Erasing the circle")


class Rectangle(Shape):

    def draw(self):
        print("Drawing a rectangle")

    def fill_color(self, color):
        print(f"Filling the rectangle with {color} color")

    def erase(self):
        print("Erasing the rectangle")


class Creator(ABC):

    @abstractmethod
    def create_product(self):
        pass

    def render(self):
        product = self.create_product()
        product.draw()
        product.fill_color("blue")
        product.erase()


class CircleCreator(Creator):
    def create_product(self):
        return Circle()


class RectangleCreator(Creator):
    def create_product(self):
        return Rectangle()


if __name__ == "__main__":
    circle_creator = CircleCreator()
    circle_creator.render()

    rectangle_creator = RectangleCreator()
    rectangle_creator.render()