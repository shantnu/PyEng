#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

salary = np.fromfile("salaries.txt", dtype=int, sep=",")

names = np.genfromtxt("names.txt", dtype='str', delimiter=",")

x = np.arange(len(names))

# Bar chart has to be with number on x axis, so we
# plot against x, but replace 'x' with names using 'xticks'
plt.bar(x, salary)
plt.xticks(x, names)

plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")

plt.show()

print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))

salaries_new = salary[2:-2]
names_new = names[2:-2]

x = range(len(names_new))

plt.bar(x, salaries_new)
plt.xticks(x, names_new)

plt.show()

print(np.max(salaries_new), np.min(salaries_new), np.average(salaries_new))
