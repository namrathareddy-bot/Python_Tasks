import numpy as np
nums=np.random.randint(1,100,10)
result=nums[nums%5==0]
print("Original array:",nums)
print("sorted result:",result)
