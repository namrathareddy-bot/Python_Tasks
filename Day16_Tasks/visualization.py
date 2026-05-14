import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales=np.array([100,200,150,300])
products=["A","B","C","D"]

df=pd.DataFrame({"Products":products,"Sales":sales})
print(df)

plt.figure(figsize=(10,5))

#line
plt.subplot(1,3,1)
plt.plot(products, sales, marker='o')
plt.title("Trend")

#Bar
plt.subplot(1,3,2)
plt.bar(products, sales)
plt.title("Comparision")

#pie
plt.subplot(1,3,3)
plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title("Distribution")

plt.tight_layout()
plt.show()
