def find_minimum(arr):
    print(arr)
    min_element = arr[0]
    min_idx = 0
    for idx, element in enumerate(arr):
        if element < min_element:
            min_element = element
            min_idx = idx
    return min_element, min_idx


def selection_sort(arr):
    for i in range(len(arr) - 1):
        anchor = i
        min_element, idx = find_minimum(arr[i:])
        print(min_element, idx)

        arr[i], arr[idx + i] = arr[idx + i], arr[i]
        i += 1

    pass


if __name__ == '__main__':
    numbers = [11, 22, 2, 5, 88, 30]
    selection_sort(numbers)
    print(numbers)
