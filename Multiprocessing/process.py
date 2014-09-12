#!/usr/bin/python
import multiprocessing
import random
from gen_rand import gen_random_data

if __name__ == '__main__':
    for x in range(4):
        process = multiprocessing.Process(target=gen_random_data)
        process.start()