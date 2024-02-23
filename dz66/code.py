class Node:

    def __init__(self, task_id, name, priority=None):
        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.next = None

    def __str__(self):
        return f"Task№{self.task_id}: {self.name}, priority -> {self.priority}"


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.completed_tasks = 0

    def enqueue(self, task_id, name, priority):
        new_task = Node(task_id, name, priority)
        if not self.head or new_task.priority < self.head.priority:
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next and current.next.priority <= new_task.priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task
            if not new_task.next:
                self.tail = new_task
        self.size += 1

    def dequeue(self):
        if not self.head:
            print("Queue is empty")
        else:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            self.completed_tasks += 1
            if not self.head:
                self.tail = None
            return temp

    @property
    def size_(self):
        return self.size

    def is_empty(self):
        return not self.head


queue = Queue()
queue.enqueue(1, "Підготувати звіт про продажі", 3)
queue.enqueue(2, "Відправити заказ клієнту A", 1)
queue.enqueue(3, "Сформувати презентацію для команди", 3)
queue.enqueue(4, "Зателефонувати постачальнику щодо поставки товару", 2)
queue.enqueue(5, "Відправити заказ клієнту B", 1)
queue.enqueue(6, "Замовити нове обладнання для офісу", 2)
print("Size is", queue.size_)
print("Completed task", queue.completed_tasks)
print(queue.dequeue())
print(queue.dequeue())
print("Completed task", queue.completed_tasks)
print("Size is", queue.size_)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print("Completed task", queue.completed_tasks)
print(queue.dequeue())
print("Size is", queue.size_)
print("Is empty?", queue.is_empty())
