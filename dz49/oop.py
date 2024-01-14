class Person:
    '''Опис класу.
       Ці рядки автоматично можна продивитись функцією  help'''

    def __init__(self, name='xxx', money=0):
        self.name = name
        self.money = money
        self.friends = []
        print('A new Person is born! =', self.name)

    def __str__(self):
        return self.name + str(self.money)

    def giveMoney(self, delta):
        self.money += delta
        print('Рахунок {} поповнено на суму {}, всього = {}'.format(self.name, delta, self.money))

    def know(self, person):
        self.friends.append(person)

    def is_know(self, person):
        return person in self.friends


print(Person.__doc__)
A = Person()
B = Person()
C = Person('Petro', 100)
D = Person('Ira', 30)
print('A: Name = {}, money = {:.2f}'.format(A.name, A.money))
print('B: Name = {}, money = {:.2f}'.format(B.name, B.money))

A.name = 'Ivan'
B.name = 'Anna'
B.money = 100.2852

A.giveMoney(50.127)
B.giveMoney(40)

print('A: Name = {}, money = {:.2f}'.format(A.name, A.money))
print('B: Name = {}, money = {:.2f}'.format(B.name, B.money))

for person in [A, B, C, D]:
    if person.money < 50:
        person.giveMoney(100)

for person in [A, B, C, D]:
    print(person)

A.know(B)
A.know(C)
print('Is A know to B?', B.is_know(A))
print('Is B know to A?', A.is_know(B))
