# Python Tuple is a collection of objects separated by commas. In
# some ways, a tuple is similar to a list in terms of indexing, nested
# objects, and repetition but a tuple is immutable, unlike lists which are mutable.


var = ("Geeks", "for", "Geeks")
print("Value in Var[0] = ", var[0])
print("Value in Var[1] = ", var[1])
print("Value in Var[2] = ", var[2])
# Value in Var[0] =  Geeks
# Value in Var[1] =  for
# Value in Var[2] =  Geeks

print("Value in Var[-3] = ", var[-3])
print("Value in Var[-2] = ", var[-2])
print("Value in Var[-1] = ", var[-1])
# Value in Var[-3] =  Geeks
# Value in Var[-2] =  for
# Value in Var[-1] =  Geeks

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
print(tuple1 + tuple2)
# ((0, 1, 2, 3), ('python', 'geek'))

tuple1 = (0, 1, 2, 3)
# tuple1[0] = 4 Not allowed, IMMUTABLE
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3)
# ((0, 1, 2, 3), ('python', 'geek'))

tuple3 = ('python',) * 3
print(tuple3)
# ('python', 'python', 'python')


tuple1 = (0, 1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
# (1, 2, 3)
# (3, 2, 1, 0)
# (2, 3)

list1 = [0, 1, 2]
print(tuple(list1))
print(tuple('python'))
# (0, 1, 2)
# ('p', 'y', 't', 'h', 'o', 'n')
