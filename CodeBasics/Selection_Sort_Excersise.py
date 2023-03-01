def multilevel_selection_sort(elements, sort_by_list):
    # SORT BY SECOND INDEX FIRST sort_by_list[-1::-1]
    for sort_by in sort_by_list[-1::-1]:
        for x in range(len(elements)):
            min_index = x
            for y in range(x, len(elements)):
                if elements[y][sort_by] < elements[min_index][sort_by]:
                    min_index = y
            if x != min_index:
                elements[x], elements[min_index] = elements[min_index], elements[x]


def find_min_element(arr, key, key2):
    min_element = arr[0]
    print(min_element)
    min_idx = 0
    for idx, element in enumerate(arr):
        print(min_element[key])
        if element[key] < min_element[key]:
            min_element = element
            min_idx = idx
        if element[key] == min_element[key]:
            if element[key2] < min_element[key2]:
                min_element = element
                min_idx = idx
    return min_element, min_idx


def modified_selection_sort(arr, key1, key2):
    for i in range(len(arr) - 1):
        min_element, idx = find_min_element(arr[i:], key1, key2)
        arr[i], arr[idx + i] = arr[idx + i], arr[i]
        i += 1


if __name__ == '__main__':
    dictionary_list = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    modified_selection_sort(dictionary_list, key1='First Name', key2='Last Name')
    print(dictionary_list)
