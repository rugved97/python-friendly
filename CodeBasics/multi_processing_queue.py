import multiprocessing
import time


def calc_squares(numbers, q):
    print('Calculating squares')
    for index, n in enumerate(numbers):
        time.sleep(0.2)
        print('Square: ', n * n)
        q.put(n * n)


if __name__ == '__main__':
    t = time.time()
    arr = [2, 3, 4, 5]
    queue = multiprocessing.Queue()
    process1 = multiprocessing.Process(target=calc_squares, args=(arr, queue))

    process1.start()

    process1.join()

    print('Done ', time.time() - t)
    while not queue.empty():
        print(queue.get())
