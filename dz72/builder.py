from abc import ABC, abstractmethod


class Computer:

    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.operating_system = None

    def __str__(self):
        return f"Computer: Processor={self.processor}, Memory={self.memory}, Storage={self.storage}, Graphics Card={self.graphics_card}, OS={self.operating_system}"


class Builder(ABC):

    def __init__(self):
        self.computer = Computer()

    def get_computer(self) -> Computer:
        comp = self.computer
        self.computer = Computer()
        return comp

    @abstractmethod
    def add_processor(self, processor):
        pass

    @abstractmethod
    def add_memory(self, memory):
        pass

    @abstractmethod
    def add_storage(self, storage):
        pass

    @abstractmethod
    def add_graphics_card(self, graphics_card):
        pass

    @abstractmethod
    def add_operating_system(self, operating_system):
        pass


class ComputerBuilder(Builder):

    def add_processor(self, processor):
        self.computer.processor = processor

    def add_memory(self, memory):
        self.computer.memory = memory

    def add_storage(self, storage):
        self.computer.storage = storage

    def add_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card

    def add_operating_system(self, operating_system):
        self.computer.operating_system = operating_system


class Director:

    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def build_minimal_computer(self, specs: dict) -> None:
        self.builder.add_processor(specs['processor'])
        self.builder.add_memory(specs['memory'])
        self.builder.add_storage(specs['storage'])
        self.builder.add_graphics_card(specs['graphics_card'])

    def build_full_computer(self, specs: dict) -> None:
        self.build_minimal_computer(specs)
        self.builder.add_operating_system(specs['operating_system'])


builder = ComputerBuilder()
director = Director(builder)

specs_minimal = {
    'processor': 'Intel Core i5',
    'memory': '16GB RAM',
    'storage': '512GB SSD',
    'graphics_card': 'NVIDIA GeForce RTX 3060'
}

specs_full = {
    'processor': 'Intel Core i5',
    'memory': '16GB RAM',
    'storage': '1TB HDD',
    'graphics_card': 'NVIDIA GeForce RTX 3050',
    'operating_system': 'Windows 10'
}

director.build_minimal_computer(specs_minimal)
computer_minimal = builder.get_computer()

director.build_full_computer(specs_full)
computer_full = builder.get_computer()
print("Minimal Computer:")
print(computer_minimal)
print("\nFull Computer:")
print(computer_full)