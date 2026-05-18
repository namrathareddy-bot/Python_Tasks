import pandas as pd
import matplotlib.pyplot as plt
data={
    "Month":["Jan","Feb","Mar"],
    "Store_A":[100,150,200],
    "Store_B":[90,140,210]
}
df=pd.DataFrame(data)
print(df)

#line
plt.plot(df["Month"],df["Store_A"],marker='o',label="Store_A")
plt.plot(df["Month"],df["Store_B"],marker='o',label="Store_B")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Comparision")
plt.legend()
plt.show()
