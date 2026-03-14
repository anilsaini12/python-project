
import pandas as pd
import matplotlib.pyplot as plt

movie = pd.read_csv("movies.csv")

# Dataset Inspection 
print(movie.head())
print(movie.info())
print(movie.describe())

#  Data Cleaning 
movie["Budget"] = movie["Budget"].str.replace("?", "", regex=False)
movie["Budget"] = movie["Budget"].str.replace(",", "", regex=False)
movie["Budget"] = movie["Budget"].astype(int)

# Convert Budget to Million (for better graph readability)
movie["Budget_Million"] = movie["Budget"] / 1000000

#  Dashboard 
plt.figure(figsize=(15,8))
plt.suptitle("Movie Data Analysis Dashboard", fontsize=16)

# 1 Genre Distribution
plt.subplot(2,3,1)
genre_count = movie["Genre"].value_counts()
plt.bar(genre_count.index, genre_count.values)
plt.title("Movies per Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=75)
plt.grid(True)

# 2 Runtime Distribution
plt.subplot(2,3,2)
plt.hist(movie["Run Time"], bins=10)
plt.title("Runtime Distribution")
plt.xlabel("Run Time (minutes)")
plt.ylabel("Number of Movies")
plt.grid(True)

# 3 Budget vs Oscar Wins
plt.subplot(2,3,3)
plt.scatter(movie["Budget_Million"], movie["Oscar Wins"])
plt.title("Budget vs Oscar Wins")
plt.xlabel("Budget (Million)")
plt.ylabel("Oscar Wins")
plt.grid(True)

# 4 Director vs Total Oscar Wins
plt.subplot(2,3,4)
director_oscar = movie.groupby("Director")["Oscar Wins"].sum()
plt.bar(director_oscar.index, director_oscar.values)
plt.title("Director vs Total Oscar Wins")
plt.xlabel("Director")
plt.ylabel("Total Oscars")
plt.xticks(rotation=90)
plt.grid(True)

# 5 Genre vs Average Runtime
plt.subplot(2,3,5)
genre_runtime = movie.groupby("Genre")["Run Time"].mean()
plt.bar(genre_runtime.index, genre_runtime.values)
plt.title("Genre vs Avg Runtime")
plt.xlabel("Genre")
plt.ylabel("Average Runtime")
plt.xticks(rotation=75)
plt.grid(True)

# 6 Runtime vs Oscar Wins
plt.subplot(2,3,6)
plt.scatter(movie["Run Time"], movie["Oscar Wins"])
plt.title("Runtime vs Oscar Wins")
plt.xlabel("Run Time (minutes)")
plt.ylabel("Oscar Wins")
plt.grid(True)

# Layout fix
plt.tight_layout(rect=[0,0,1,0.95])

plt.show()