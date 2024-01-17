class Book:
    def __init__(self, title, author):
        self._attributes = {"title": title, "author": author}

    def __getattr__(self, name):
        print(f"Call __getattr__ {name}")
        if name in self._attributes:
            return self._attributes[name]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        print(f"Call __setattr__ with {name=} {value=}")
        if name == "_attributes":
            super().__setattr__(name, value)
        else:
            self._attributes[name] = value

    def __delattr__(self, name):
        print(f"Call __delattr__ {name}")
        if name in self._attributes:
            del self._attributes[name]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __getattribute__(self, name):
        print(f"Call __getattribute__ with {name}")
        if name == "secret":
            return "Access to 'secret' if forbidden."
        elif name in ("_attribute", "__dict__"):
            return super().__getattribute__(name)
        else:
            try:
                return super().__getattribute__(name)
            except AttributeError:
                return self.__getattr__(name)


book = Book("Python Programming", "John Zelle")
book.year = 2016
print(book.__dict__)
print(book.secret)
