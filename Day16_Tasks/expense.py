import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
expenses=np.array([500,200,300])
labels=["Food","Rent","Travel"]

#pie
plt.pie(expenses,labels=labels,autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.show()
