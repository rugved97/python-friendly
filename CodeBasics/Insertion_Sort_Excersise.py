def running_median(elements):
    print(elements[0])
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > anchor:
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = anchor

        if i % 2 != 0:
            mid_point = i // 2
            average = (elements[mid_point] + elements[mid_point + 1]) / 2
            print(average)
        else:
            print(elements[i // 2])


if __name__ == '__main__':
    numbers = [2, 1, 5, 7, 2, 0, 5]
    running_median(numbers)
    print(numbers)
