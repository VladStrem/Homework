class LoginRequired:

    def __init__(self, permission):
        self.permission = permission

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.permission in permissions:
                func(*args, **kwargs)
            else:
                raise ValueError(f"Нема доступу для користувача {self.permission}")
        return wrapper


permissions = ["user", "admin"]


@LoginRequired("vlad")
def data():
    print("secret data")


data()