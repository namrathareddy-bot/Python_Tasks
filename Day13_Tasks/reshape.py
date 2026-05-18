import numpy as np
data=np.arange(1,13)
reshaped=data.reshape(3,4)
avg_each_row=np.mean(reshaped,axis=1)
print("after reshaping:",reshaped)
print(" row avgerages:",avg_each_row)
