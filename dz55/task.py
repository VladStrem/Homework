import math


class Vector:
    def __init__(self, x, y, z):
        if not all(isinstance(coord, (int, float)) for coord in (x, y, z)):
            raise ValueError("Координати повинні бути числового типу.")

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise ValueError("Підтримується тільки множення на число або вектор.")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))

    def __int__(self):
        return int(self.__len__())

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __bool__(self):
        return self.__len__() != 0


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 == v2)
print(v1 != v2)

print(v1 + v2)
print(v1 - v2)

v1 += v2
print(v1)

v1 *= 2
print(v1)

print(v1 * v2)

print(len(v1))
print(int(v1))

v3 = -v1
print(v3)

print(bool(v1))
print(bool(Vector(0, 0, 0)))