import multiprocessing
import time


def deposit(bal, lock_var):
    print('Deposit')
    for i in range(5):
        time.sleep(0.2)
        lock_var.acquire()
        print('IN deposit', bal.value)
        bal.value += 1
        print('After IN deposit', bal.value)
        lock_var.release()


def withdraw(bal, lock_var):
    print('Withdraw')
    for i in range(5):
        time.sleep(0.2)
        lock_var.acquire()
        print('IN Withdraw', bal.value)
        bal.value -= 1
        print('After IN Withdraw', bal.value)
        lock_var.release()


if __name__ == '__main__':
    t = time.time()
    lock = multiprocessing.Lock()
    balance = multiprocessing.Value('i', 5)
    process1 = multiprocessing.Process(target=deposit, args=(balance, lock))
    process2 = multiprocessing.Process(target=withdraw, args=(balance, lock))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('Done ', time.time() - t)
    print(balance.value)
