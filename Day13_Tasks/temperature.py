import numpy as np
temps=np.array([28,32,35,31,29,40,38])
#condition
hot_days=temps>30
#indices where condition is True
indices=np.where(hot_days)
print("Temperature>30:",temps[hot_days])
print("Indices:",indices[0])
