import time
import threading

square_result = []


def calc_squares(numbers):
    print('Calculating Squares..')

    for number in numbers:
        time.sleep(0.2)
        square_result.append(number * number)
        print("Square:", number * number)


def calc_cubes(numbers):
    print('Calculating Cubes..')

    for number in numbers:
        time.sleep(0.5)
        print('Square result in cube thread', square_result)
        print("Cube:", number * number * number)


if __name__ == '__main__':
    arr = [2, 3, 4, 5]
    t = time.time()
    # Without Threading
    # calc_squares(arr)
    # calc_cubes(arr)

    t1 = threading.Thread(target=calc_squares, args=(arr,))
    t2 = threading.Thread(target=calc_cubes, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Finished in ', time.time() - t)
    # Finished in 1.6268079280853271
    # Finished in 0.8018560409545898
