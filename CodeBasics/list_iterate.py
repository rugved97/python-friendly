if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    # Using for loop
    for i in list1:
        print(i)

    # 1
    # 3
    # 5
    # 7
    # 9

    list2 = [2, 4, 6, 8, 10]
    length = len(list2)
    # Iterating the index
    # same as 'for i in range(len(list))'
    for i in range(length):
        print(list2[i])
    # 2
    # 4
    # 6
    # 8
    # 10

    list3 = [10, 20, 30, 40, 50]
    length = len(list3)
    i = 0
    # Iterating using while loop
    while i < length:
        print(list3[i])
        i += 1

    # List Comprehension
    list4 = ['apple', 'figs', 'cherry']

    # Using list comprehension
    [print(i) for i in list4]
    # apple
    # figs
    # cherry

    # Method #5: Using enumerate()
    # If we want to convert the list into an iterable list of tuples (or get the index based on a condition check,
    # for example in linear search you might need to save the index of minimum element), you can use the enumerate()
    # function.

    list5 = [1, 3, 5, 7, 9]

    # Using enumerate()
    for i, val in enumerate(list5):
        print(i, ",", val)

    # 0, 1
    # 1, 3
    # 2, 5
    # 3, 7
    # 4, 9

    list6 = [('name', 10), ('name1', 20), ('name3', 30), ]

    for i, val in enumerate(list6):
        print(i, ",", val[0])
