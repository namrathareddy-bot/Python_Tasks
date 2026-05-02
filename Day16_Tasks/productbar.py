import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales=np.array([50,80,40])
products=["Pen","Book","Pencil"]

df=pd.DataFrame({"Products":products,"Sales":sales})
print(df)

#bar
plt.bar(df["Products"],df["Sales"])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()
