def bubble_sort(array):
    size = len(array)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    numbers = [43, 23, 1, 5, 67, 51, 10]
    bubble_sort(numbers)
    print(numbers)
