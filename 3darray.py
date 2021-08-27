import numpy
ls1 = [[1, 2], [3, 4]]
ls2 = [[4, 5], [6, 7]]
q1 = numpy.array(ls1)
q2 = numpy.array(ls2)
q = numpy.array([q1, q1])
print(q1)
print(q2)
print(q)
print(q.ndim)
