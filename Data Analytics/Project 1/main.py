# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#=======================================================================================
#  Scenario-1--Basic Data Loading & Cleaning
#=======================================================================================
# 1.1 Load the dataset
df = pd.read_csv('railway_gauges 1.csv')

# 1.2 Display first 5 rows
print("First 5 rows of the dataset:")
#view sample data
print(df.head())

# Display column names
print("\nColumn names in the dataset:")
#checks column
print(df.columns)

# 1.3 Check for missing values
print("\nMissing values in each column:")
# missing values check
print(df.isnull().sum())

# Replace missing values with 0
df.fillna(0, inplace=True)

print("\nMissing values after replacing with 0:")
print(df.isnull().sum())

# 1.4 Convert gauge columns to numeric type
gauge_columns = ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge', 'Total']

for col in gauge_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Replace any NaN created during conversion(clean NaN)
df.fillna(0, inplace=True)

print("\nData types after conversion:")
print(df.dtypes)


# =======================================================================================
#  Scenario-2--Simple Visualization
# =======================================================================================
#2.1 Extract Year and Total columns
# 2.1 Select required columns (Year and Total tracks)
data = df[['Year', 'Total']].copy()

# 2.2 Extract year part + convert to numeric (cleaning )
data['Year'] = data['Year'].str[:4]
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

# convert Total to numeric (safe conversion)
data['Total'] = pd.to_numeric(data['Total'], errors='coerce')

# remove invalid/missing rows after conversion
data.dropna(inplace=True)

# 2.3 Plot line graph (trend visualization)
plt.plot(data['Year'], data['Total'], marker='o')

# add chart title
plt.title('Total Railway Track Growth Over Years')

# X and Y axis labels
plt.xlabel('Year')
plt.ylabel('Total Track Length')

# 2.4 Display graph and observe trend (increase/decrease)
plt.grid(True)
#plt.savefig("simplevisualization.png")
plt.show()


# show sample data (verification)
print(data.head())

# final observation
print("\nFinal Observation:")
print("The trend is increasing (Railway track length is growing over the years)")

#=======================================================================================
#  Scenario-3--Filtering & Bar Chart
#=======================================================================================
# 3.1 Filter the dataset for years after 2000
df['Year'] = df['Year'].str[:4].astype(int)
recent_df = df[df['Year'] > 2000]

# 3.2 Select Broad Gauge, Metre Gauge, and Narrow Gauge
gauge_data = recent_df[['Year', 'Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].copy()

# handle missing values if any
gauge_data.fillna(0, inplace=True)

# 3.3 Plot a grouped bar chart comparing all three gauges
x = range(len(gauge_data['Year']))

plt.bar(x, gauge_data['Broad Gauge'], width=0.3, label='Broad Gauge')
plt.bar([i + 0.3 for i in x], gauge_data['Metre Gauge'], width=0.3, label='Metre Gauge')
plt.bar([i + 0.6 for i in x], gauge_data['Narrow Gauge'], width=0.3, label='Narrow Gauge')

# 3.4 Add legend and proper labels
plt.xticks([i + 0.3 for i in x], gauge_data['Year'], rotation=45)
plt.xlabel("Year")
plt.ylabel("Number of Tracks")
plt.title("Railway Gauge Comparison After 2000")
plt.legend()

plt.tight_layout()
#plt.savefig("filter&bar.png")
plt.show()


# 3.5 Identify which gauge dominates in recent years
print("Broad Gauge dominates in recent years")


#=======================================================================================
#Scenario 4: Feature Engineering + Pie Chart
#=======================================================================================

# 4.1 Calculate total sum of each gauge across all years
totals = df[['Broad Gauge','Metre Gauge','Narrow Gauge']].sum()

# 4.2 Create a new structure (Series/DataFrame) for totals
print("Gauge Totals:\n", totals)

# 4.3 Plot a pie chart showing percentage contribution
plt.figure(figsize=(7,7))

plt.pie(
    totals,
    labels=totals.index,
# 4.4 Add percentage labels (autopct)
    autopct='%1.1f%%',

    startangle=140
)

plt.title("Gauge Contribution (%)")
#plt.savefig("piechart.png")
plt.show()

# 4.5 Interpret which gauge contributes the most
print("Highest contributing gauge:", totals.idxmax())


#=======================================================================================
#Scenario 5: Advanced Analysis + Multiple Graphs
#=======================================================================================

# 5.1 Create new columns:
#    % Broad Gauge, % Metre Gauge, % Narrow Gauge
df['% Broad Gauge'] = (df['Broad Gauge'] / df['Total']) * 100
df['% Metre Gauge'] = (df['Metre Gauge'] / df['Total']) * 100
df['% Narrow Gauge'] = (df['Narrow Gauge'] / df['Total']) * 100


# 5.2 Use NumPy (np.diff) to calculate yearly growth of Total tracks
growth = np.diff(df['Total'])
df['Growth'] = [None] + list(growth)

# 5.3.1 Plot Line Graph for all gauges
plt.figure(figsize=(10,5))

plt.plot(df['Year'], df['Broad Gauge'], label='Broad Gauge')
plt.plot(df['Year'], df['Metre Gauge'], label='Metre Gauge')
plt.plot(df['Year'], df['Narrow Gauge'], label='Narrow Gauge')

plt.xticks(rotation=90)
plt.title("Gauge Trends Over Time")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.grid()

#plt.savefig("linegr.png")

plt.show()


# 5.3.2 Plot Stacked Bar Chart showing composition
plt.figure(figsize=(12,6))

plt.bar(df['Year'], df['Broad Gauge'], label='Broad Gauge')
plt.bar(df['Year'], df['Metre Gauge'],
        bottom=df['Broad Gauge'], label='Metre Gauge')
plt.bar(df['Year'], df['Narrow Gauge'],
        bottom=df['Broad Gauge'] + df['Metre Gauge'],
        label='Narrow Gauge')

plt.xticks(rotation=90)
plt.title("Gauge Composition Over Time")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()

#plt.savefig("5barchart.png")
plt.show()



# 5.4.1 Highlight Years with highest growth
max_growth_year = df.loc[df['Growth'].idxmax(), 'Year']
print("Year with highest growth:", max_growth_year)

# 5.4.2 Highlight decline in any gauge
print("Metre Gauge declining years:",
      df['Year'][df['Metre Gauge'].diff() < 0].tolist())

print("Narrow Gauge declining years:",
      df['Year'][df['Narrow Gauge'].diff() < 0].tolist())

# 5.5 Provide final conclusion:
print("\nConclusion:")
print("The railway system is shifting towards a single dominant gauge (Broad Gauge).")