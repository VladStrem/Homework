class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, max_size=-1):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.max_size != -1 and self.size == self.max_size

    def push(self, data):
        if not self.is_full():
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
            self.size += 1
            print(f'Pushed: {data}')
        else:
            print('Stack is full. Cannot push.')

    def pop(self):
        if not self.is_empty():
            popped_data = self.top.data
            self.top = self.top.next
            self.size -= 1
            print(f'Popped: {popped_data}')
            return popped_data
        else:
            print('Stack is empty. Cannot pop.')

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            print('Stack is empty. Cannot peek.')

    def clear(self):
        self.top = None
        self.size = 0
        print('Stack cleared.')

    def display_menu(self):
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Is Empty?")
        print("4. Is Full?")
        print("5. Size")
        print("6. Peek")
        print("7. Clear")
        print("8. Exit")

    def run_menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                data = input("Enter the string to push: ")
                self.push(data)
            elif choice == "2":
                self.pop()
            elif choice == "3":
                print(f'Is Empty: {self.is_empty()}')
            elif choice == "4":
                print(f'Is Full: {self.is_full()}')
            elif choice == "5":
                print(f'Size: {self.size}')
            elif choice == "6":
                print(f'Peek: {self.peek()}')
            elif choice == "7":
                self.clear()
            elif choice == "8":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    max_size = int(input("Enter the maximum size of the stack (-1 for unlimited): "))
    stack = Stack(max_size)
    stack.run_menu()
