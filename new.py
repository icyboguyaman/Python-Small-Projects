import numpy
t = numpy.ones((4, 3))
print(t.sum())
print(t.max())
print(numpy.exp(t))
print(numpy.sqrt(t))
print(numpy.sin(t))
print(numpy.log10(t))
print(t.ravel())
print(t.T)
t.resize((6, 2))
print(t)
print(numpy.random.random((2, 3)))

