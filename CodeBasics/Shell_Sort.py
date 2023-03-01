def shell_sort(arr):
    gap = len(arr) // 2

    while gap > 0:

        for i in range(gap, len(arr)):
            j = i
            anchor = arr[i]
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = anchor
        gap = gap // 2


if __name__ == '__main__':
    numbers = [11, 22, 2, 5, 88, 30]
    shell_sort(numbers)
    print(numbers)
