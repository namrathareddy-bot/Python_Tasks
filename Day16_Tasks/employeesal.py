import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries=np.array([25000,30000,28000,40000,50000,35000])
departments=["HR","IT","HR","IT","SALES","SALES"]
df=pd.DataFrame({"Department":departments,"Salary":salaries})
print(df)

#line
plt.plot(salaries,marker='o')
plt.title("Salary Trend")
plt.show()

#bar
df.groupby("Department")["Salary"].mean().plot(kind='bar')
plt.title("Dept-wise salary")
plt.show()

#pie
dept_counts=df["Department"].value_counts()
plt.pie(dept_counts,labels=dept_counts.index,autopct='%1.1f%%')
plt.title("Department Diatribution")
plt.show()

#histogram
plt.hist(salaries,bins=5)
plt.title("Salary Diatribution")
plt.show()

#scatterplot
plt.scatter(departments,salaries)
plt.title("Index vs Salary")
plt.show()
