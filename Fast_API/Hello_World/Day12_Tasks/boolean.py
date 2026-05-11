import numpy as np
salary=np.array([25000,40000,15000,50000,30000])
#count
count=np.sum(salary>30000)
filter_val=salary[salary>30000]
print("salary above 30000:",filter_val)
print("count:",count)
