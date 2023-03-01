def find_index_of_occurrence(numbers_list, value, left_index, right_index):
    occurrence = []
    mid_index = (left_index + right_index) // 2
    if left_index <= right_index:
        if numbers_list[mid_index] == value:
            occurrence.append(mid_index)
            index_l = find_index_of_occurrence(numbers_list, value, left_index, mid_index - 1)
            index_r = find_index_of_occurrence(numbers_list, value, mid_index + 1, right_index)
            if index_r:
                occurrence += index_r
            if index_l:
                occurrence += index_l
        else:
            if numbers_list[mid_index] < value:
                return find_index_of_occurrence(numbers_list, value, mid_index + 1, right_index)
            else:
                return find_index_of_occurrence(numbers_list, value, left_index, mid_index - 1)

        return occurrence
    return


def find_all_occurrences_scanning(number_list, value, left_index, right_index):
    occurrences = []
    mid_index = (left_index + right_index) // 2

    if left_index <= right_index:
        if number_list[mid_index] == value:
            occurrences.append(mid_index)

            i = mid_index - 1
            while i >= 0:
                if number_list[i] == value:
                    occurrences.append(i)
                    i -= 1
                else:
                    break
            i = mid_index + 1
            while i < len(number_list):
                if number_list[i] == value:
                    occurrences.append(i)
                    i += 1
                else:
                    break

            return sorted(occurrences)

        if number_list[mid_index] < value:
            return find_all_occurrences_scanning(number_list, value, mid_index + 1, right_index)
        else:
            return find_all_occurrences_scanning(number_list, value, left_index, mid_index - 1)


if __name__ == '__main__':
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    all_index = find_index_of_occurrence(numbers, number_to_find, 0, len(numbers) - 1)
    print(f'All occurrences {all_index} of {number_to_find}')

    all_index_scanning = find_all_occurrences_scanning(numbers, number_to_find, 0, len(numbers) - 1)
    print(f'All occurrences {all_index} of {number_to_find}')
