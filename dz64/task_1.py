class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_to_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_head(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def remove_from_tail(self):
        if self.is_empty():
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def remove_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    return self.remove_from_head()
                elif current == self.tail:
                    return self.remove_from_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return current.data
            current = current.next
        return None

    def add_at_index(self, index, data):
        if index == 0:
            self.add_to_head(data)
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    return False
                current = current.next

            if current is None:
                return False

            new_node = Node(data)
            new_node.prev = current
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            else:
                self.tail = new_node
            current.next = new_node
            return True

    def traverse_forward(self):
        current = self.head
        while current:
            print(f"{current.data} <-> ", end="")
            current = current.next
        print()

    def traverse_backward(self):
        current = self.tail
        while current:
            print(f"{current.data} <-> ", end="")
            current = current.prev
        print()

    def clear(self):
        self.head = self.tail = None


dll = DoublyLinkedList()

dll.add_to_head(1)
dll.add_to_tail(2)
dll.add_to_tail(3)
dll.traverse_forward()
dll.traverse_backward()
dll.remove_from_head()
dll.remove_from_tail()
dll.traverse_forward()
dll.add_at_index(0, 1)
dll.add_at_index(2, 3)
dll.traverse_forward()
dll.remove_by_value(2)
dll.traverse_forward()
dll.clear()
dll.traverse_forward()
