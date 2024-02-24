from abc import ABC, abstractmethod


class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

    def display_info(self):
        print(f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}")

    def save_to_file(self, file_path):
        with open(file_path, mode='w', encoding="utf-8") as file:
            file.write(f"{self.product_id},{self.name},{self.category},{self.price}\n")


class IProductRepository(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def remove_product(self, product_id):
        pass

    @abstractmethod
    def update_price(self, product_id, new_price):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_products_by_category(self, category):
        pass


class ProductRepository(IProductRepository):
    def __init__(self, file_path="products.txt"):
        self.products = []
        self.file_path = file_path
        self._load_products_from_file()

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]

    def update_price(self, product_id, new_price):
        for product in self.products:
            if product.product_id == product_id:
                product.price = new_price

    def get_product_by_id(self, product_id):
        return next((product for product in self.products if product.product_id == product_id), None)

    def get_products_by_category(self, category):
        return [product for product in self.products if product.category == category]

    def _update_file(self):
        with open(self.file_path, mode="w", encoding="utf-8") as file:
            for product in self.products:
                file.write(f"{product.product_id},{product.name},{product.category},{product.price}\n")

    def _load_products_from_file(self):
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 4:
                        product = Product(int(data[0]), data[1], data[2], float(data[3]))
                        self.products.append(product)
        except FileNotFoundError:
            pass


class Store:
    def __init__(self, file_path="products.txt"):
        self.product_repository = ProductRepository(file_path)

    def add_product_to_store(self, product: Product):
        self.product_repository.add_product(product)
        print(f"Товар {product.name} додано до магазину.")
        self._display_store_info()

    def remove_product_from_store(self, product_id):
        removed_product = self.product_repository.get_product_by_id(product_id)
        self.product_repository.remove_product(product_id)
        if removed_product:
            print(f"Товар {removed_product.name} видалено з магазину.")
            self._display_store_info()

    def update_product_price(self, product_id, new_price):
        self.product_repository.update_price(product_id, new_price)

    def get_product_by_id(self, product_id):
        return self.product_repository.get_product_by_id(product_id)

    def get_products_by_category(self, category):
        return self.product_repository.get_products_by_category(category)

    def get_total_products_count(self):
        return len(self.product_repository.products)

    def calculate_category_total_cost(self, category):
        category_products = self.get_products_by_category(category)
        return sum(product.price for product in category_products)

    def calculate_total_cost(self):
        return sum(product.price for product in self.product_repository.products)

    def _display_store_info(self):
        print("=== Інформація про магазин ===")
        print("Загальна кількість товарів у магазині:", self.get_total_products_count())
        print("Загальна вартість товарів у магазині:", self.calculate_total_cost())
        print("=============================")


if __name__ == "__main__":
    laptop = Product(1, "Лаптоп", "Електроніка", 1200)
    laptop.display_info()

    laptop.save_to_file("products.txt")

    store = Store()
    store.add_product_to_store(Product(1, "Лаптоп", "Електроніка", 1200))
    store.add_product_to_store(Product(2, "Книга", "Книги", 20))
    store.add_product_to_store(Product(3, "Футболка", "Одяг", 30))
    laptop = store.get_product_by_id(1)
    if laptop:
        laptop.display_info()

    store.remove_product_from_store(2)
