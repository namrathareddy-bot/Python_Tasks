import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales=np.array([100,150,200,180,220,300])
months=["Jan","Feb","Mar","Apr","May","Jun"]

df=pd.DataFrame({"Month":months,"Sales":sales})
print(df)

#line graph
plt.plot(months,sales,marker='o')
plt.title("Sales Trend")
plt.show()

#bar graph
plt.bar(months,sales)
plt.title("Monthly sales")
plt.show()

#pie chart
plt.pie(sales,labels=months,autopct='%1.1f%%')
plt.title("Sales Contriution")
plt.show()

#histogram
plt.hist(sales,bins=5)
plt.title("Sales Distribution")
plt.show()

#scatterplot
# plt.scatter(range(len(sales)),sales)
# plt.title("Index vs Sales")
# plt.show()
plt.scatter(months, sales)
plt.title("Index vs Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
