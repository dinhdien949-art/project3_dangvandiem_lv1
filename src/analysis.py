import pandas as pd
import os

CLEANED_PATH = "/Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/data/cleaned/tmdb_movies_cleaned.csv"
OUTPUT_PATH = "/Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/data/output"

# Load cleaned data
df = pd.read_csv(CLEANED_PATH, parse_dates=["release_date"])

print("Data loaded:", df.shape)

# Create output folder
os.makedirs(OUTPUT_PATH, exist_ok=True)

# ================================
# TASK 1: Sort by release_date DESC
# ================================
df_sorted = df.sort_values(by="release_date", ascending=False)
df_sorted.to_csv(os.path.join(OUTPUT_PATH, "q1_movies_sorted_by_release_date.csv"), index=False)
print("Saved: q1_movies_sorted_by_release_date.csv")

# ================================
# TASK 2: Movies with vote_average > 7.5
# ================================
df_high_rating = df[df["vote_average"] > 7.5]
df_high_rating.to_csv(os.path.join(OUTPUT_PATH, "q2_movies_rating_above_7_5.csv"), index=False)
print("Saved: q2_movies_rating_above_7_5.csv")

# ================================
# TASK 3: Highest & Lowest revenue movie
# ================================
max_revenue_movie = df.loc[df["revenue"].idxmax(), ["original_title", "revenue"]]
min_revenue_movie = df.loc[df["revenue"].idxmin(), ["original_title", "revenue"]]

q3_result = pd.DataFrame({
    "type": ["highest_revenue", "lowest_revenue"],
    "movie": [max_revenue_movie["original_title"], min_revenue_movie["original_title"]],
    "revenue": [max_revenue_movie["revenue"], min_revenue_movie["revenue"]]
})

q3_result.to_csv(os.path.join(OUTPUT_PATH, "q3_highest_lowest_revenue.csv"), index=False)
print("Saved: q3_highest_lowest_revenue.csv")

# ================================
# TASK 4: Total revenue of all movies
# ================================
total_revenue = df["revenue"].sum()

q4_result = pd.DataFrame({
    "total_revenue": [total_revenue]
})

q4_result.to_csv(os.path.join(OUTPUT_PATH, "q4_total_revenue.csv"), index=False)
print("Saved: q4_total_revenue.csv")

# ================================
# TASK 5: Top 10 most profitable movies
# ================================
df["profit"] = df["revenue"] - df["budget"]

top10_profit = (
    df.sort_values(by="profit", ascending=False)
      .head(10)[["original_title", "budget", "revenue", "profit"]]
)

top10_profit.to_csv(os.path.join(OUTPUT_PATH, "q5_top10_profitable_movies.csv"), index=False)
print("Saved: q5_top10_profitable_movies.csv")

# ================================
# TASK 6: Director & Actor with most movies
# ================================

# ---- Director ----
top_director = (
    df.dropna(subset=["director"])
      .groupby("director")["id"]
      .count()
      .sort_values(ascending=False)
      .reset_index()
      .rename(columns={"id": "movie_count"})
      .head(1)
)

top_director.to_csv(os.path.join(OUTPUT_PATH, "q6_top_director.csv"), index=False)

# ---- Actor ----
df_cast = df.dropna(subset=["cast"]).copy()
df_cast["cast_list"] = df_cast["cast"].str.split("|")

top_actor = (
    df_cast.explode("cast_list")["cast_list"]
      .value_counts()
      .reset_index()
      .rename(columns={"index": "actor", "cast_list": "movie_count"})
      .head(1)
)

top_actor.to_csv(os.path.join(OUTPUT_PATH, "q6_top_actor.csv"), index=False)

print("Saved: q6_top_director.csv and q6_top_actor.csv")

# ================================
# TASK 7: Count movies by genre
# ================================
df_genre = df.dropna(subset=["genres"]).copy()
df_genre["genre_list"] = df_genre["genres"].str.split("|")

genre_counts = (
    df_genre.explode("genre_list")["genre_list"]
      .value_counts()
      .reset_index()
      .rename(columns={"index": "genre", "genre_list": "movie_count"})
)

genre_counts.to_csv(os.path.join(OUTPUT_PATH, "q7_movie_count_by_genre.csv"), index=False)
print("Saved: q7_movie_count_by_genre.csv")

print("\nANALYSIS COMPLETED!")
