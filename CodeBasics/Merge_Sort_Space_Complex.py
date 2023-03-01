def merge_sort_w_space(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort_w_space(left)
    merge_sort_w_space(right)
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    idx_a = idx_b = idx_c = 0

    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a] < b[idx_b]:
            arr[idx_c] = a[idx_a]
            idx_c += 1
            idx_a += 1
        else:
            arr[idx_c] = b[idx_b]
            idx_c += 1
            idx_b += 1

    while idx_a < len(a):
        arr[idx_c] = a[idx_a]
        idx_c += 1
        idx_a += 1
    while idx_b < len(b):
        arr[idx_c] = b[idx_b]
        idx_c += 1
        idx_b += 1


if __name__ == '__main__':
    numbers = [11, 22, 2, 5, 88, 30]

    merge_sort_w_space(numbers)
    print(numbers)
