import numpy as np
data=np.array([27,9,15,21,8,12])
data=np.sort(data)
a,b=np.split(data,2)
print("After sorting the data:",data)
print("After splitting into 2 equal parts:",a,b)
print("sum of first part a:",np.sum(a),"sum of second part b:",np.sum(b))
