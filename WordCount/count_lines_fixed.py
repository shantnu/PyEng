#! /usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

f = open("birds.txt", "r")
data = f.read()
f.close()

lines = data.split("\n")
print("Wrong: The number of lines is", len(lines))

for l in lines:
    if not l:
        # Can also do this: if len(l) == 0
        lines.remove(l)
print("Right: The number of lines is", len(lines))
