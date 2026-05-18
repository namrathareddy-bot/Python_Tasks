import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=np.array([100,np.nan,200,150,np.nan,300])

series=pd.Series(data)
print("Original:\n",series)

#Replace nan with mean
mean_val=series.mean()
series.fillna(mean_val, inplace=True)

print("Cleaned:\n",series)

#line
plt.plot(series,marker='o')
plt.title("Cleaned Data Trend")
plt.show()

#bar for val>avg
above_avg=series[series>mean_val]
plt.bar(range(len(above_avg)),above_avg)
plt.title("Vlues>Average")
plt.show()
