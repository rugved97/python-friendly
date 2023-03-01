import time
from collections import deque
import threading


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


orders_to_be_served = Queue()


def place_order(orders_placed):
    for order in orders_placed:
        time.sleep(0.5)
        print('Adding order', order)
        orders_to_be_served.enqueue(order)


def serve_order():
    while not orders_to_be_served.is_empty():
        time.sleep(2)
        print(orders_to_be_served.dequeue())


if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    place_order_thread = threading.Thread(target=place_order, args=(orders,))
    server_order_thread = threading.Thread(target=serve_order)

    place_order_thread.start()
    time.sleep(1)
    server_order_thread.start()

    place_order_thread.join()
    server_order_thread.join()
