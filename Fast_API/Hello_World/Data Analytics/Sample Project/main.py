import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load CSV file
df = pd.read_csv("/Users/namratha/Desktop/python tasks/Data Analytics/Sample Project/railway_gauges.csv")

print(df.head())

# find which year had the max installations
print(df.iloc[[df['Total'].idxmax()]])

# Plot data using bar chart
df = df.drop('Total', axis=1)

ax = df.plot(x='Year', kind="bar")

plt.xticks(rotation=70)
plt.xlabel('Year')
plt.ylabel('Number of Tracks')
plt.title('Gauges: Number of railway tracks installed per year')

plt.savefig('rail_gauges.png')
plt.show()

