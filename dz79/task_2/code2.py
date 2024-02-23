import datetime


def log_call(file):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file, mode="a", encoding="utf-8") as log_file:
                log_file.write(f"Method '{func.__name__}' called at {current_time}\n")

            result = func(self, *args, *kwargs)
            return result
        return wrapper
    return decorator


class MyClass:

    @log_call(file="test.log")
    def info(self):
        print("This is my method")


my_instance = MyClass()
my_instance.info()