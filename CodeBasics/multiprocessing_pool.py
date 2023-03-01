import time
from multiprocessing import Pool


def f(numbers):
    sum = 0
    for n in range(10000000):
        sum += n * n
    return sum


def f2(n):
    return n * n


def f3(n):
    sum = 0
    for x in range(1000):
        sum += x * x
    return sum


if __name__ == '__main__':
    arr = [2, 3, 4, 5]
    t1 = time.time()
    result = []
    for x in range(10):
        result.append(f(range(10000)))

    # result = f(range(10000))
    print('Done', time.time() - t1)

    pool1 = Pool()
    t2 = time.time()
    pool1.map(f, range(10))
    pool1.close()
    pool1.join()
    print('Done with pool', time.time() - t2)

    array = [1, 2, 3, 4, 5]
    result = []
    for n in array:
        result.append(f2(n))
    print(result)

    pool2 = Pool()
    result2 = pool2.map(f2, array)  # Apply each function to an iterable
    pool2.close()
    pool2.join()
    print(result2)

    # result == result2 == [1, 4, 9, 16, 25]

    t3 = time.time()
    pool3 = Pool()
    pool3.map(f3, range(10000))
    pool3.close()
    pool3.join()
    print('Done pool3', time.time() - t3)

    t3_without_pool = time.time()
    for i in range(10000):
        f3(0)

    print('Done without pool', time.time() - t3_without_pool)
