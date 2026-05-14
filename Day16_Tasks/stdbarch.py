import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks=np.array([85,70,90,60])
names=["A","B","C","D"]

df=pd.DataFrame({"Name":names, "Marks":marks})
print(df)

#bar graph
plt.bar(df["Name"],df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()
