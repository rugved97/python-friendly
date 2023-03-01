import collections


class Stack:
    def __init__(self):
        self.container = collections.deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        if self.is_empty():
            print('Stack EMPTY')
            return
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def print(self):
        print(self.container)


if __name__ == '__main__':
    stack = Stack()

    stack.push(3)
    stack.push(4)
    stack.print()

    stack.pop()
    stack.print()

    stack.push(5)
    stack.push(7)
    
    print(stack.peek())
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
