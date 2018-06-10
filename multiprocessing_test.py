#!/usr/bin/env python3
# Ver_1.0.0_3
from multiprocessing import Process
from time import time


def time_and_exec(func, name):
    '''
    Create, execute, terminate and join a Process(func),
    whilst timing its execution.
    '''
    before = time()
    p1 = Process()
    p1.start()
    func()
    p1.terminate()
    p1.join()
    print(f"Process {name} took: {round(time() - before, 8)}")
    return


def func_lc():
    '''
    Evaluates how List Comprehensions work.
    '''
    return [x + 1 for x in range(0, 10000000, 1)]


def func_lamb():
    '''
    Executes a Lambda function mapping 'x' in range.
    '''
    return list(map(lambda x: x + 1, range(0, 10000000, 1)))


def main():
    '''
    Main function.
    '''
    time_and_exec(func_lamb, 'Lamb')
    time_and_exec(func_lc, 'LC')
    print('All Done!')


if __name__ == '__main__':
    main()
