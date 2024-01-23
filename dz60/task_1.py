def init(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender


def greet(self):
    print("Hi, my name is", self.name)


def description(self):
    print(f"Person<{self.name}, {self.age}, {self.gender}>")


Student = type("Student", (), {'__slots__': ['name', 'age', 'gender'],
                               '__init__': init, 'greet': greet, 'description': description})


student_instance = Student("John", 25, "Male")
student_instance.greet()
student_instance.description()