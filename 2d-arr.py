import numpy as np
ls = [[1, 2, 3], [4, 5, 3], [5, 3, 2]]
arr = np.array(ls)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.mean())
print(np.median(ls))
print(arr.std())
print(arr[1, 1])
print(arr[:, 1])
print(arr[:1, 1])
print(arr[1, 1:])
print(arr[1:, 1:])
print()
for q in np.ravel(arr):
    print(q)
for i in arr.flat:
    print(i)
print(arr < 5)
print(arr[arr < 5])
print(arr[arr % 2 == 0])

