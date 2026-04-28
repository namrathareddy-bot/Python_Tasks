#project title:scottish hill analysis
# Using NumPy, Pandas, and Matplotlib for analysis
import numpy as np
import pandas as pd


#Scenario 1: Data Loading & Basic Cleaning

"""Tasks: 
1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows 
○ Column names 
3. Check for missing values in: 
○ Height 
○ Region 
4. Fill missing values: 
○ Height → use mean 
○ Region → use mode 
5. Convert Height column to numeric if required."""

#1.1 Load the dataset using Pandas.
df = pd.read_csv("scottish_hills.csv")
#1,2 Display first 5 rows and column names
print("First 5 rows:\n", df.head())
print("\nColumn names:\n", df.columns)
# Clean column names (important)
df.columns = df.columns.str.strip().str.title()

# 3. Create Region column (if not available)
if "Region" not in df.columns:
    print("\nRegion column not found → Creating using Latitude & Longitude")

    # Midpoints
    lat_mid = df["Latitude"].median()
    lon_mid = df["Longitude"].median()

    # Function to assign region
    def assign_region(row):
        lat = row["Latitude"]
        lon = row["Longitude"]
        
        if lat >= lat_mid and lon >= lon_mid:
            return "North-East"
        elif lat >= lat_mid and lon < lon_mid:
            return "North-West"
        elif lat < lat_mid and lon >= lon_mid:
            return "South-East"
        else:
            return "South-West"

    # Apply function
    df["Region"] = df.apply(assign_region, axis=1)
# 4. Convert Height to numeric (before checking missing)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
#1.3. Check for missing values height and region 
print("\nMissing values:")
print(df[["Height", "Region"]].isnull().sum())
# 1.4. Handle missing values
df["Height"] = df["Height"].fillna(df["Height"].mean())
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])

print("\nAfter handling missing values:")
print(df[["Height", "Region"]].head())

# 1.5. Convert Height to numeric (if needed)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")

print("\nData types after conversion:")
print(df.dtypes)
 

#=================================================================================
# Scenario 2
#=================================================================================

# Load dataset
df = pd.read_csv("scottish_hills.csv")

# Clean column names
df.columns = df.columns.str.strip().str.title()

# Create Region column if missing
if "Region" not in df.columns:
    lat_mid = df["Latitude"].median()
    lon_mid = df["Longitude"].median()

    def assign_region(row):
        lat = row["Latitude"]
        lon = row["Longitude"]

        if lat >= lat_mid and lon >= lon_mid:
            return "North-East"
        elif lat >= lat_mid and lon < lon_mid:
            return "North-West"
        elif lat < lat_mid and lon >= lon_mid:
            return "South-East"
        else:
            return "South-West"

    df["Region"] = df.apply(assign_region, axis=1)

# Convert Height to numeric
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")

# Fill missing values
df["Height"] = df["Height"].fillna(df["Height"].mean())
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("scottish_hills.csv")

# Clean column names
df.columns = df.columns.str.strip().str.title()

# Convert Height to numeric
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")

# Fill missing Height values
df["Height"] = df["Height"].fillna(df["Height"].mean())

# 1. Select required columns
data = df[["Hill Name", "Height"]]

# 2. Take first 10 rows
data = data.head(10)

# 3. Convert Height to NumPy array
heights = data["Height"].to_numpy()

# 4. Plot line graph
plt.figure(figsize=(10, 6))
plt.plot(range(len(heights)), heights, marker='o')

# 5. Add title and labels
plt.title("Height Variation of First 10 Hills")
plt.xlabel("Index (0–9)")
plt.ylabel("Height")

plt.grid(True)

# 6. Save the graph
plt.savefig("hill_heights_line.png")

# Show plot
plt.show()