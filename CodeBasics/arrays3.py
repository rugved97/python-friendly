def odd_numbers():
    ip = input('Enter max number')
    ip = int(ip)
    a = []
    for i in range(1, ip):
        if i % 2 != 0:
            a.append(i)

    return a

    # max = int(input("Enter max number: "))
    #
    # odd_numbers = []
    #
    # for i in range(1, max):
    #     if i % 2 == 1:
    #         odd_numbers.append(i)
    #
    # print("Odd numbers: ", odd_numbers)


print('odd_numbers', odd_numbers())
