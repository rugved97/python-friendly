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


def reverse_string(string):
    stack = Stack()
    for letter in string:
        stack.push(letter)
    result = ''
    while not stack.is_empty():
        result += stack.pop()

    print(result)


def is_balanced(string):
    stack = Stack()

    parenthesis = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    for char in string:
        if not stack.is_empty():
            if stack.peek() in parenthesis and parenthesis[stack.peek()] == char:
                stack.pop()
                continue
        if char in ['(', '[', '{', ')', ']', '}']:
            stack.push(char)

    print(stack.is_empty())


# def is_match(ch1, ch2):
#     match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#     return match_dict[ch1] == ch2
#
#
# def is_balanced(s):
#     stack = Stack()
#     for ch in s:
#         if ch=='(' or ch=='{' or ch == '[':
#             stack.push(ch)
#         if ch==')' or ch=='}' or ch == ']':
#             if stack.size()==0:
#                 return False
#             if not is_match(ch,stack.pop()):
#                 return False
#
#     return stack.size()==0

if __name__ == '__main__':
    reverse_string("We will conquere COVID-19")
    reverse_string("I am the king")
    is_balanced("({a+b})")
    is_balanced("))((a+b}{")
    is_balanced("((a+b))")
    is_balanced("))")
    is_balanced("[a+b]*(x+2y)*{gg+kk}")
