import multiprocessing
import time

squares_result = []


def calc_squares(numbers, result):
    print('Calculating squares')
    global squares_result
    for index, n in enumerate(numbers):
        time.sleep(0.2)
        print('Square: ', n * n)
        squares_result.append(n * n)

        result[index] = n * n

    print('Squares within process', squares_result)


def calc_cube(numbers, result, v):
    print('Calculating cubes')
    v.value = 5.67
    for n in numbers:
        time.sleep(0.2)
        print(result[:])
        print('Cube: ', n * n * n)


if __name__ == '__main__':
    t = time.time()
    arr = [2, 3, 4, 5]
    process_results = multiprocessing.Array('i', 4)
    process_value = multiprocessing.Value('d', 0.0)
    process1 = multiprocessing.Process(target=calc_squares, args=(arr, process_results))
    process2 = multiprocessing.Process(target=calc_cube, args=(arr, process_results, process_value))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('Done ', time.time() - t)
    print('Result', squares_result)
    # Need to print it as below
    print('Process result', process_results[:])
    print('Print value', process_value.value)
