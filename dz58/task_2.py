class UsernameDescriptor:
    def __get__(self, instance, owner):
        return instance._username

    def __set__(self, instance, value):
        if not (4 <= len(value) <= 10 and value[0].isalpha() and value.isalnum()):
            raise ValueError("Invalid username format")
        instance._username = value


class PasswordDescriptor:
    def __get__(self, instance, owner):
        return instance._password

    def __set__(self, instance, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        instance._password = value


class User:
    username = UsernameDescriptor()
    password = PasswordDescriptor()

    def __init__(self, username, password):
        self.username = username
        self.password = password


try:
    user1 = User("user123", "pass")
except ValueError as e:
    print(f"Error: {e}")

try:
    user2 = User("validUser", "password123")
    print(f"Username: {user2.username}, Password: {user2.password}")
except ValueError as e:
    print(f"Error: {e}")