a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

print('a = ', a)
print('a[len(a) - 1] = ', a[len(a) - 1])  # lobster

# a[6]
# Traceback (most recent call last):
# IndexError: list index out of range


print('a[-1] = ', a[-1])  # lobster
# a[-8]
# Traceback (most recent call last):
# IndexError: list index out of range

# ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# Slicing is indexing syntax that extracts a portion from a list. If a is a list, then a[m:n] returns the portion of a:
#
# Starting with position m
# Up to but not including n
# Negative indexing can also be used

print('a[2:5] = ', a[2:5])  # ['bacon', 'tomato', 'ham']

print('a[-5:-2] = ', a[-5:-2])  # ['egg', 'bacon', 'tomato']

a[2:5] = 'chicken'
print('a[2:5] = ''chicken ---> ', a)  # ['spam', 'egg', 'c', 'h', 'i', 'c', 'k', 'e', 'n', 'lobster']

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
a[2:5] = ['chicken']
print('a[2:5] = [''chicken] ---> ', a)

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print('a[-5:-2] == a[1:4] = ', a[-5:-2] == a[1:4])  # True

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# Omitting the first and/or last index:
#
# Omitting the first index a[:n] starts the slice at the beginning of the list.
# Omitting the last index a[m:] extends the slice from the first index m to the end of the list.
# Omitting both indexes a[:] returns a copy of the entire list, but unlike with a string, it’s a copy,
# not a reference to the same object.

print('a[2:len(a)] = ', a[2:len(a)])  # ['bacon', 'tomato', 'ham', 'lobster']

print('a[2:] = ', a[2:])  # ['bacon', 'tomato', 'ham', 'lobster']

print('a == a[:] = ', a == a[:])  # True

print('a is a[:] = ', a is a[:])  # False

# ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# A stride can be added to your slice notation. Using an additional : and a third index designates a stride
# (also called a step) in your slice notation. The stride can be either positive or negative:

print('a[0:6:2] = ', a[0:6:2])  # ['spam', 'bacon', 'ham']
print('a[6:0:-2] = ', a[6:0:-2])  # ['lobster', 'tomato', 'egg']
print('a[::-1] = ', a[::-1])  # ['lobster', 'ham', 'tomato', 'bacon', 'egg', 'spam']
