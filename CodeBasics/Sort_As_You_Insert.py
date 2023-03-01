def index_to_insert(array, element):
    index = 0
    for item in array:
        if item < element:
            index += 1
        else:
            break
    return index


def insert_sort_now(array, element):
    idx = index_to_insert(array, element)
    return array[0:idx] + [element] + array[idx:]


if __name__ == '__main__':
    stream = []

    while True:
        inp = int(input())

        stream = insert_sort_now(stream, inp)
        print(stream)
