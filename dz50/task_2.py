class Car:
    manufacturer = "Mercedes Club"
    total = 0

    def __init__(self, model, year, engine_volume, color, price):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.price = price
        Car.total += price

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model} {self.color}-${self.price}"

    def change_color(self, new_color):
        self.color = new_color

    def change_price(self, new_price):
        Car.total -= self.price
        self.price = new_price
        Car.total += new_price

    @classmethod
    def get_total(cls):
        return cls.total


car_1 = Car("Civic", 2022, 1.8, "blue", 25000)
car_2 = Car("Accord", 2021, 2.0, "red", 35000)

print(car_1)
print(car_2)

print(f"Total Price: ${Car.get_total()}")
car_1.change_color("green")
print(car_1)
car_2.change_price(38000)
print(car_2)
print(f"Updated Total Price: ${Car.get_total()}")