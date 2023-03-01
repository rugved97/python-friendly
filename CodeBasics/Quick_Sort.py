def swap(a, b, array):
    # array[a], array[b] = array[b], array[a]
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def partition(array, start_index, end_index):
    pivot_index = start_index
    # start_index = pivot_index + 1
    # end_index = len(array) - 1
    while start_index < end_index:
        while start_index < end_index and array[start_index] <= array[pivot_index]:
            start_index += 1

        while array[end_index] > array[pivot_index]:
            end_index -= 1

        if start_index < end_index:
            swap(start_index, end_index, array)
    swap(pivot_index, end_index, array)
    return end_index


def quick_sort(elements, start, end):
    if start < end:
        partition_index = partition(elements, start, end)
        quick_sort(elements, start, partition_index - 1)
        quick_sort(elements, partition_index + 1, end)


if __name__ == '__main__':
    numbers = [11, 22, 2, 5, 88, 30]
    quick_sort(numbers, start=0, end=len(numbers) - 1)
    print(numbers)
