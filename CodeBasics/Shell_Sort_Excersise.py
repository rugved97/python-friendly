def modified_shell_sort(arr):
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            anchor = arr[i]
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap

            if arr[j - gap] == anchor:
                arr[j - gap] = -1
            arr[j] = anchor

        gap = gap // 2
    arr = [x for x in arr if x != -1]
    return arr


def modified_shell_sort_w_index(arr):
    # IMPORTANT
    div = 2
    # IMPORTANT
    gap = len(arr) // div
    size = len(arr)
    while gap > 0:
        index_to_delete = []
        for i in range(gap, size):
            j = i
            anchor = arr[i]
            while j >= gap and arr[j - gap] >= anchor:
                if arr[j - gap] == anchor:
                    index_to_delete.append(j)
                arr[j] = arr[j - gap]

                j -= gap

            arr[j] = anchor

        if index_to_delete:
            # IMPORTANT: to reverse index and pop as if you pop earlier index, array indexes change, from there on
            print(index_to_delete[-1::-1])
            for i in index_to_delete:
                print(arr)
                arr.pop(i)
                print(arr)
        # IMPORTANT
        div += 2
        # IMPORTANT
        size = len(arr)
        # IMPORTANT
        gap = size // div

    # Sort the elements of a given list using shell sort, but with a slight modification. Remove all the repeating


# occurrences of elements while sorting.
# Traditionally, when comparing two elements in shell sort, we swap if first element is bigger than second, and do
# nothing otherwise.
# In this modified shel sort with duplicate removal, we will swap if first element is bigger than second,
# and do nothing if element is smaller, but if values are same, we will delete one of the two elements we are comparing
# before starting the next pass for the reduced gap.
# For example, given the unsorted list [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3], after sorting using shell sort without
# duplicates, the sorted list would be:

if __name__ == '__main__':
    numbers = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    modified_shell_sort_w_index(numbers)
    print(numbers)
