import numpy
import random
ls = []
for i in range(4):
    temp = []
    j = 0
    while j < 3:
        a = random.randint(0, 10)
        if a % 2 == 0:
            temp.append(a)
            j += 1

    ls.append(temp)
q = numpy.array(ls)
print(q)
