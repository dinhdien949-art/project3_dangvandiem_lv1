
import pandas as pd
import os

RAW_PATH = "/Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/data/raw/tmdb_movies_raw.csv"
CLEANED_PATH = "../data/cleaned/tmdb_movies_cleaned.csv"

#Crerate Cleaned folder
os.makedirs("../data/cleaned", exist_ok=True)

def load_raw():
    return pd.read_csv(RAW_PATH)

def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate rows")
    return df

def handle_nulls(df):
    print("Handling NULL values...")

    # 1 DROP column with too many nulls
    if "homepage" in df.columns:
        df = df.drop(columns=["homepage"])
        print("Dropped column: homepage (too many nulls)")

    # 2 Fill medium-null text columns
    fill_unknown_cols = ["keywords", "production_companies", "cast", "director", "genres", "imdb_id"]

    for col in fill_unknown_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    # 3️Special handling
    if "tagline" in df.columns:
        df["tagline"] = df["tagline"].fillna("No tagline")

    if "overview" in df.columns:
        df["overview"] = df["overview"].fillna("No overview")

    return df

def standardize_dates(df):
    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(df["release_date"], format="%Y-%m-%d", errors="coerce") # chu y doan format date nay
    return df

def filter_runtime(df):
    if "runtime" in df.columns:
        before = len(df)
        df = df[(df["runtime"] >= 30) & (df["runtime"] <= 300)]
        print(f"Removed {before - len(df)} rows due to unrealistic runtime")
    return df

def save_cleaned(df):
    df.to_csv(CLEANED_PATH, index=False)
    print("Saved cleaned data to:", CLEANED_PATH)

if __name__ == "__main__":
    df = load_raw()
    df = remove_duplicates(df)
    df = handle_nulls(df)
    df = standardize_dates(df)
    df = filter_runtime(df)
    save_cleaned(df)

    print("DATA CLEANING COMPLETED!")
