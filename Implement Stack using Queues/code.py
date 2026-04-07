class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None 
        self._size = 0

    def enqueue(self, x):
        node = Node(x)
        if self._tail:
            self._tail.next = node
        self._tail = node
        if self._head is None:
            self._head = node
        self._size += 1

    def dequeue(self):
        node = self._head
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.val

    def peek(self):
        return self._head.val

    def is_empty(self):
        return self._head is None

    def size(self):
        return self._size


class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)
        # прокручуємо всі попередні елементи в кінець
        for _ in range(self.queue.size() - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self) -> int:
        return self.queue.dequeue()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
