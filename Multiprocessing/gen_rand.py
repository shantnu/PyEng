#!/usr/bin/python
import threading
import random


def gen_random_data():
    arr = []
    for i in range(1000000):
        arr.append(random.random())
    print "job done"