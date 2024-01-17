from code55 import Vector


class NewVector(Vector):
    def __getitem__(self, index):
        if index == 1:
            return self.x
        elif index == 2:
            return self.y
        elif index == 3:
            return self.z
        else:
            raise IndexError("Index out of range. Valid indices are 1, 2, 3.")

    def __setitem__(self, index, value):
        if index == 1:
            self.x = value
        elif index == 2:
            self.y = value
        elif index == 3:
            self.z = value
        else:
            raise IndexError("Index out of range. Valid indices are 1, 2, 3.")

    def __contains__(self, value):
        return value in [self.x, self.y, self.z]

    def __call__(self, value):
        return Vector(self.x + value, self.y + value, self.z + value)


try:
    v1 = NewVector(1, 2, 3)
    v2 = NewVector(4, 5, 6)
    print(v1[1])
    v1[1] = 10
    print(v1)
    print(v1.__contains__(2))
    v3 = v1(5)
    print(v3)

except ValueError as ve:
    print(f"ValueError: {ve}")
except IndexError as ie:
    print(f"IndexError: {ie}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
