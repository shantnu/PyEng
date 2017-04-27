#! /usr/bin/python

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
