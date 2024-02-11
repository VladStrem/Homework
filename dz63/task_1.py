class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == prev_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Елемент із значенням {prev_data} не знайдено")

    def delete_tail(self):
        if not self.head:
            print("Список порожній")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_head(self):
        if not self.head:
            print("Список порожній")
            return
        self.head = self.head.next

    def delete_by_value(self, value, count=1):
        if not self.head:
            print("Список порожній")
            return
        current = self.head
        prev = None
        deleted_count = 0
        while current and deleted_count < count:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                deleted_count += 1
            else:
                prev = current
            current = current.next

    def replace_value(self, old_value, new_value, replace_all=False):
        current = self.head
        replaced = False
        while current:
            if current.data == old_value:
                current.data = new_value
                replaced = True
                if not replace_all:
                    break
            current = current.next
        if not replaced:
            print(f"Елемент із значенням {old_value} не знайдено")

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def menu():
    linked_list = LinkedList()

    while True:
        print("\nМеню:")
        print("1. Додати елемент у хвіст списку")
        print("2. Додати елемент до списку на початок")
        print("3. Вставити новий елемент після елемента з певним значенням")
        print("4. Видалити елемент з хвоста списку")
        print("5. Видалити елемент з голови списку")
        print("6. Видалити елемент з певним значенням")
        print("7. Замінити значення у списку")
        print("8. Визначити розмір списку")
        print("9. Показати вміст списку")
        print("0. Вийти")

        choice = input("Введіть номер опції: ")

        if choice == '0':
            break
        elif choice == '1':
            data = input("Введіть значення для нового елемента: ")
            linked_list.append(data)
        elif choice == '2':
            data = input("Введіть значення для нового елемента: ")
            linked_list.prepend(data)
        elif choice == '3':
            prev_data = input("Введіть значення для елемента, після якого треба вставити новий: ")
            new_data = input("Введіть значення нового елемента: ")
            linked_list.insert_after(prev_data, new_data)
        elif choice == '4':
            linked_list.delete_tail()
        elif choice == '5':
            linked_list.delete_head()
        elif choice == '6':
            value = input("Введіть значення для видалення: ")
            count = int(input("Введіть кількість видалень (1 для одного видалення, більше 1 для багаторазового): "))
            linked_list.delete_by_value(value, count)
        elif choice == '7':
            old_value = input("Введіть значення, яке потрібно замінити: ")
            new_value = input("Введіть нове значення: ")
            replace_all = input("Замінити всі входження? (yes/no): ").lower() == 'yes'
            linked_list.replace_value(old_value, new_value, replace_all)
        elif choice == '8':
            print(f"Розмір списку: {linked_list.size()}")
        elif choice == '9':
            linked_list.display()
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    menu()
