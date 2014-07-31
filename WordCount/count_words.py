#! /usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

f = open("birds.txt", "r")
data = f.read()
f.close()

words = data.split(" ")
print("The words in the text are:")
print(words)
num_words = len(words)

print("The number of words is ", num_words)


lines = data.split("\n")
print("The lines in the text are:")
print(lines)

print("The number of lines is", len(lines))

