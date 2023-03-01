def merge_sort_w_space(arr, key, descending):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort_w_space(left, key, descending)
    merge_sort_w_space(right, key, descending)
    merge_two_sorted_lists(left, right, arr, key, descending)


def merge_two_sorted_lists(a, b, arr, key, desc):
    idx_a = idx_b = idx_c = 0

    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a][key] < b[idx_b][key]:
            if desc:
                arr[idx_c] = b[idx_b]
                idx_b += 1
            else:
                arr[idx_c] = a[idx_a]
                idx_a += 1
            idx_c += 1

        else:
            if desc:
                arr[idx_c] = a[idx_a]
                idx_a += 1
            else:
                arr[idx_c] = b[idx_b]
                idx_b += 1

            idx_c += 1

    while idx_a < len(a):
        arr[idx_c] = a[idx_a]
        idx_c += 1
        idx_a += 1
    while idx_b < len(b):
        arr[idx_c] = b[idx_b]
        idx_c += 1
        idx_b += 1


if __name__ == '__main__':
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]
    merge_sort_w_space(elements, key='time_hours', descending=True)
    print(elements)
