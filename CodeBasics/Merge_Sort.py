def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge_two_sorted_lists(left_sorted, right_sorted)


def merge_two_sorted_lists(a, b):
    sorted_list = []
    idx_a = idx_b = 0

    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a] < b[idx_b]:
            sorted_list.append(a[idx_a])
            idx_a += 1
        else:
            sorted_list.append(b[idx_b])
            idx_b += 1

    while idx_a < len(a):
        sorted_list.append(a[idx_a])
        idx_a += 1
    while idx_b < len(b):
        sorted_list.append(b[idx_b])
        idx_b += 1
    return sorted_list


if __name__ == '__main__':
    numbers = [11, 22, 2, 5, 88, 30]

    print(merge_sort(numbers))
