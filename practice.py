import pandas as pd
import numpy as np

arr = np.arange(20).reshape(5, 4)
axis_ABC = np.array(['A', 'A', 'B', 'C', 'C'])

print(arr[axis_ABC == "A"])
print(arr[axis_ABC == "A", :2])
print(arr[~(axis_ABC == "A")])
print(arr[(axis_ABC != "A") & (axis_ABC != "B")])

arr = np.arange(20).reshape(5, 4)
arr[arr <= 7] = 0
arr[np.logical_and(arr > 7, arr < 16)] = 10

a = np.arange(15).reshape(5, 3)

a = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06])
np.round(a)
np.round(a, 1)
np.rint(a)
np.fix(a)
np.ceil(a)
np.floor(a)
np.trunc(a)

b = np.array([1, 2, 3, 4])
c = np.array([[1, 2], [3, 4]])

np.prod(c, axis=1)
np.prod(c, axis=0)

d = np.array([[1, 2], [3, np.nan]])
np.nanprod(d, axis=0)
np.nanprod(d, axis=1)

e = np.array([1, 2, 3, 4])
f = np.array([[1, 2, 3], [4, 5, 6]])
np.cumprod(e)






