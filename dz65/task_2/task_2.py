class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None


def check_brackets(input_string):
    stack = Stack()

    for char in input_string:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()


print(check_brackets("((()))"))
print(check_brackets("(()()())"))
print(check_brackets("((())"))
print(check_brackets("()()()"))
