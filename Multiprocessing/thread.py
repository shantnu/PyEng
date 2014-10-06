#!/usr/bin/python
import threading
from gen_rand import gen_random_data

if __name__ == '__main__':
    for x in range(4):
        process = threading.Thread(target=gen_random_data)
        process.start()