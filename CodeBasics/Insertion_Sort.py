def insertion_sort(elements):
    for index in range(1, len(elements)):
        anchor = elements[index]
        j = index - 1
        while j >= 0 and elements[j] > anchor:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor


if __name__ == '__main__':
    numbers = [21, 38, 29, 17, 4, 25]
    insertion_sort(numbers)
    print(numbers)
