#=================================================================
#Title:IGN
#=================================================================
#=================================================================
#Import libraries
#=================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   


#=================================================================
# Scenario 1: Data Loading & Preprocessing
#=================================================================
# 1. Load the dataset using Pandas.
# 2. Display:
# ○ First 5 rows (head())
# ○ Last 5 rows (tail())
# ○ Shape of dataset
# 3. Remove the unnecessary column:
# ○ "Unnamed: 0" (index column)
# 4. Check for missing values in:
# ○ score, genre, platform
# 5. Handle missing values:
# ○ Fill numeric column score with mean
# ○ Fill categorical column genre with mode
# 6. Ensure correct data types:
# ○ score → float
# ○ release_year, release_month, release_day → integer
#=================================================================
# 1. Load the dataset using Pandas.
df = pd.read_csv("/Users/namratha/Desktop/python tasks/Data Analytics/Project 2/ign.csv")
# 2. Display:
# ○ First 5 rows (head())
# ○ Last 5 rows (tail())
# ○ Shape of dataset
print("First 5 rows:\n",df.head())
print("\nLast 5 rows:\n",df.tail())
print("\nShape of dataset:\n",df.shape)
#3. Remove the unnecessary column:
# ○ "Unnamed: 0" (index column)
if "Unamed: 0" in df.columns:
    df=df.drop(columns=["Unamed: 0"])
# 4. Check for missing values in:
# ○ score, genre, platform
print("\nMissing values:\n",df[["score","genre","platform"]].isnull().sum())
# 5. Handle missing values:
# ○ Fill numeric column score with mean
# ○ Fill categorical column genre with mode
df["score"]=df["score"].fillna(df["score"].mean())
df["genre"]=df["genre"].fillna(df["genre"].mode()[0])
# 6. Ensure correct data types:
# ○ score → float
# ○ release_year, release_month, release_day → integer
# 6. Fix data types
df["score"] = df["score"].astype(float)
df["release_year"] = df["release_year"].astype(int)
df["release_month"] = df["release_month"].astype(int)
df["release_day"] = df["release_day"].astype(int)

# Final check
print("\nData types:\n", df.dtypes)

#=================================================================
#Scenario 2: Line Graph (Score Trend) + Save
#=================================================================
# 1. Group data by release_year.
# 2. Calculate average score per year using Pandas.
# 3. Convert results into NumPy arrays.
# 4. Plot a line graph:
# ○ X-axis → release_year
# ○ Y-axis → average score
# 5. Add:
# ○ Title: "Average Game Score Over Years"
# ○ Axis labels
# 6. Save the graph: plt.savefig("avg_score_trend.png")
#=================================================================
# 1. Group data by release_year.&# 2. Calculate average score per year using Pandas.
avg_score=df.groupby("release_year")["score"].mean()
# 3. Convert results into NumPy arrays.
years = avg_score.index.to_numpy()
scores = avg_score.values
# 4. Plot a line graph:
# ○ X-axis → release_year
# ○ Y-axis → average score
plt.figure(figsize=(8,5))  
plt.plot(years, scores, marker='o')
# 5. Add:
# ○ Title: "Average Game Score Over Years"
# ○ Axis labels
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Year")
# 6. Save the graph: plt.savefig("avg_score_trend.png")
#plt.savefig("avg_score_trend.png")
plt.show()


#=================================================================
#�� Scenario 3: Filtering + Bar Chart + Save
#=================================================================
# 1. Filter dataset where:
# ○ score > 7
# 2. Count number of high-rated games per platform.
# 3. Select top 10 platforms using Pandas.
# 4. Convert data into NumPy arrays.
# 5. Plot a bar chart:
# ○ X-axis → platform
# ○ Y-axis → count of games
# 6. Rotate x-axis labels for readability.
# Save the graph: plt.savefig("top_platforms_bar.png")
#=================================================================
# 1. Filter dataset where:
# ○ score > 7
high_rated=df[df["score"]>7]
# 2. Count number of high-rated games per platform.
platform_counts=high_rated["platform"].value_counts()
# 3. Select top 10 platforms using Pandas.
top10_platform=platform_counts.head(10)
# 4. Convert data into NumPy arrays.
platforms=top10_platform.index.to_numpy()
counts=top10_platform.values
# 5. Plot a bar chart:
# ○ X-axis → platform
# ○ Y-axis → count of games
plt.figure(figsize=(10,5))
plt.bar(platforms,counts)
# 6. Rotate x-axis labels for readability.
plt.xticks(rotation=45)
           # Labels and title
plt.xlabel("Platform")
plt.ylabel("Number of High Rated Games")
plt.title("Top 10 Platforms by High Rated Games")

# Save graph
#plt.savefig("top_platforms_bar.png")

# Show graph
plt.show()


#=================================================================
#�� Scenario 4: Aggregation + Pie Chart + Save
#=================================================================
# 1. Count the number of games per genre.
# 2. Select top 5 genres using Pandas.
# 3. Prepare labels and values.
# 4. Plot a pie chart:
# ○ Labels → genre
# ○ Values → count
# 5. Add percentage labels (autopct).
# Save the graph: plt.savefig("genre_distribution.png")
#=================================================================
# 1. Count the number of games per genre.
genre_counts=df["genre"].value_counts()
# 2. Select top 5 genres using Pandas.
top_genres=genre_counts.head(5)
# 3. Prepare labels and values.
labels=top_genres.index
values=top_genres.values
# 4. Plot pie chart
plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct='%1.1f%%')

# Title
plt.title("Top 5 Game Genres Distribution")

# Save the graph
#plt.savefig("genre_distribution.png")

# Show chart
plt.show()

#=================================================================
#Scenario 5: Advanced Analysis + Multiple Graphs
#=================================================================
#-----------------------------------------------------------------
# Part 1: Feature Engineering
#-----------------------------------------------------------------
# 1. Create a new column:
# ○ score_category:
# ■ score >= 9 → "Excellent"
# ■ 7 <= score < 9 → "Good"
# ■ < 7 → "Average"
# 2. Convert editors_choice:
# ○ Y → 1, N → 0
#-----------------------------------------------------------------
# 1. Create score_category
def categorize(score):
    if score >= 9:
        return "Excellent"
    elif score >= 7:
        return "Good"
    else:
        return "Average"

df["score_category"] = df["score"].apply(categorize)
# 2. Convert editors_choice (Y/N → 1/0)
df["editors_choice"] = df["editors_choice"].map({"Y": 1, "N": 0})

#-----------------------------------------------------------------
# Part 2: NumPy Analysis
#-----------------------------------------------------------------
#3. Use NumPy to:
# ○ Calculate yearly score growth using np.diff() on average yearly scores
#-----------------------------------------------------------------
# Average score per year
yearly_avg = df.groupby("release_year")["score"].mean()

# Calculate growth using np.diff()
score_growth = np.diff(yearly_avg.values)

print("Yearly Score Growth:\n", score_growth)

#-----------------------------------------------------------------
#  Part 3: Visualizations
#-----------------------------------------------------------------
# Line Graph
# 4. Plot trend of:
# ○ Average score per release_year
# Stacked Bar Chart
# 5. Show count of:
# ○ score_category per releaseyear
# Histogram
# 6. Plot distribution of:
# ○ score
#-----------------------------------------------------------------
# 4. Line Graph (Score Trend)
plt.figure(figsize=(8,5))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o')
plt.title("Average Score Trend")
plt.xlabel("Year")
plt.ylabel("Average Score")
plt.savefig("score_trend.png")
plt.show()

# 5. Stacked Bar Chart (score_category per year)
category_counts = df.groupby(["release_year", "score_category"]).size().unstack()

category_counts.plot(kind="bar", stacked=True, figsize=(10,6))
plt.title("Score Category Distribution per Year")
plt.xlabel("Year")
plt.ylabel("Number of Games")
plt.savefig("score_category_stacked.png")
plt.show()

# 6. Histogram (Score Distribution)
plt.figure(figsize=(7,5))
plt.hist(df["score"], bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("score_distribution.png")
plt.show()

#-----------------------------------------------------------------
# �� Part 5: Insights
#-----------------------------------------------------------------
# Identify:
# ● Which years had highest scores
# ● Whether high scores increased over time
# ● If editors_choice correlates with high scores
#-----------------------------------------------------------------
# Highest scoring year
best_year = yearly_avg.idxmax()
print("Year with highest average score:", best_year)

# Correlation with editors_choice
correlation = df["score"].corr(df["editors_choice"])
# print("Correlation between score and editors_choice:", correlation)