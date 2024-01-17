class Size:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return len(instance.name)


class Person:

    size_name = Size()

    def __init__(self, name):
        self.name = name


person_1 = Person("John")
print("Size name =", person_1.size_name)
person_2 = Person("Alice")
print("Size name =", person_2.size_name)