def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list)

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if number_to_find == numbers_list[mid_index]:
            return mid_index
        if number_to_find < numbers_list[mid_index]:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    return -1


def binary_search_recursive_mutable(numbers_list, number_to_find):
    mid = len(numbers_list) // 2
    if number_to_find == numbers_list[mid]:
        return True

    if mid == 0:
        return False
    if number_to_find < numbers_list[mid]:
        return binary_search_recursive_mutable(numbers_list[:mid], number_to_find)
    else:
        return binary_search_recursive_mutable(numbers_list[mid + 1:], number_to_find)


def binary_search_recursive_immutable(numbers_list, number_to_find, left_index, right_index):
    mid_index = (left_index + right_index) // 2
    if left_index <= right_index:
        if number_to_find == numbers_list[mid_index]:
            return mid_index
        if number_to_find < numbers_list[mid_index]:
            return binary_search_recursive_immutable(numbers_list, number_to_find, left_index, mid_index - 1)
        else:
            return binary_search_recursive_immutable(numbers_list, number_to_find, left_index + 1, right_index)

    return -1


if __name__ == '__main__':
    numbers = [12, 14, 15, 17, 27, 32, 123]

    index_linear = linear_search(numbers, 14)
    index_binary = binary_search(numbers, 89)
    recursive_status = binary_search_recursive_mutable(numbers, 456456)
    index_recursive = binary_search_recursive_immutable(numbers, 12313, 0, len(numbers) - 1)

    print(f'Element found at index {index_linear} by linear search')
    print(f'Element found at index {index_binary} by binary search')
    print(f'Element found {recursive_status} by recursive search mutable')
    print(f'Element found at index {index_recursive} by recursive search ')
