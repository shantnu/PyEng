#!/usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

f = open("birds.txt", "r")
data = f.read()
f.close()

print(data)
