class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, x):
        node = Node(x)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.val

    def peek(self):
        return self._top.val

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._size


class MyQueue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def _move(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def pop(self) -> int:
        self._move()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move()
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
