def swap(a, b, array):
    # array[a], array[b] = array[b], array[a]
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def partition(array, start_index, end_index):
    partition_index = start_index
    pivot_index = end_index
    while array[partition_index] < array[pivot_index]:
        partition_index += 1

    iterator = partition_index + 1
    while iterator < end_index and array[iterator] > array[pivot_index]:
        iterator += 1
    if iterator < pivot_index:
        swap(partition_index, iterator, array)
        partition_index += 1

    swap(partition_index, pivot_index, array)
    return partition_index


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


if __name__ == '__main__':
    numbers = [11, 22, 2, 5, 88, 30]
    quick_sort(numbers, start=0, end=len(numbers) - 1)
    print(numbers)
