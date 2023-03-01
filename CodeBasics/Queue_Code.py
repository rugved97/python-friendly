from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        if self.is_empty():
            print('QUEUE EMPTY')
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def print(self):
        print(self.buffer)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.print()

    queue.dequeue()
    queue.print()

    queue.dequeue()
    queue.dequeue()
