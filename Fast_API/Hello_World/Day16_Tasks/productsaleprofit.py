import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales=np.array([200,300,250,400,350])
profit=np.array([50,70,60,90,80])
products=["A","B","C","D","E"]

df=pd.DataFrame({"Products":products,"Sales":sales,"Profit":profit})
print(df)

#line
plt.plot(products,sales,marker='o')
plt.title("Sales Trend")
plt.show()

#bar 
plt.bar(products,sales)
plt.title("Product vs Sales")
plt.show()

#pie
plt.pie(sales,labels=products,autopct='%1.1f%%')
plt.title("Sales Contribution")
plt.show()

#hist
plt.hist(profit,bins=5)
plt.title("Profit Distribution")
plt.show()

#scatterplot
plt.scatter(sales,profit)
plt.title("Sales vs Profit")
plt.show()
