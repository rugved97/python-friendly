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

    def front(self):
        return self.buffer[-1]


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)

    for n in range(10):
        popped = queue.dequeue()
        print(popped)
        queue.enqueue(str(popped) + '0')
        queue.enqueue(str(popped) + '1')
