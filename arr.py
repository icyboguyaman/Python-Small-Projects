import numpy
t = [1, 2, 3, 4, 5]
print(t)
q = numpy.array(t, dtype=numpy.int64)
print(q, " ", type(q))
print(q.ndim)
print(q.shape)
print(q.size)
print(q.dtype)
