import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks=np.array([45,67,89,56,72,91,38])
students=["A","B","C","D","E","F","G"]

df=pd.DataFrame({"Student":students, "Marks":marks})
print(df)

#line graph
plt.plot(df["Student"],df["Marks"],marker='o')
plt.title("Marks Trend")
plt.show()

#bar graph
plt.bar(df["Student"],df["Marks"])
plt.title("Student vs Marks")
plt.show()

#pie chart(p/f)
pass_fail=["Pass" if m > 50 else "Fail" for m in marks]
counts=pd.Series(pass_fail).value_counts()
plt.pie(counts,labels=counts.index,autopct='%1.1f%%')
plt.title("Pass vs Fail")
plt.show()

#Histogram
plt.hist(marks,bins=5)
plt.title("Marks Distribution")
plt.show()

#scatterplot
plt.scater(range(len(marks)),marks)
plt.title("Index vs Marks")
plt.show()
