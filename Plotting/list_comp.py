#! /usr/bin/python

import numpy as np

def main():
    x = [5,10,15,20,25]

    # declare y as an empty list
    y = []

    # The not so good way
    for counter in x:
        y.append(counter / 5)

    print("\nOld fashioned way: x = {} y = {} \n".format(x, y))


    # The Pythonic way
    # Using list comprehensions
    z = [n/5 for n in x]
    print("List Comprehensions: x = {} z = {} \n".format(x, z))

    # Finally, numpy
    try:
        a = x / 5
    except:
        print("No, you can't do that with regular Python lists\n")

    a = np.array(x)
    b = a / 5

    print("With Numpy: a = {} b = {} \n".format(a, b))

    return "With Numpy: a = {} b = {} \n".format(a, b)

if __name__ == "__main__":
    main()