import numpy as np
data = [5,10,15,20,25,30]
dataset = np.array(data)
print("The data is: ",dataset)
processors = np.array_split(dataset,3)
print("Array after splitting into 3 parts is: \n",processors)
