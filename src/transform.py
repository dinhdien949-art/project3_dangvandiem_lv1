import os
import pandas as pd

CLEANED_PATH = "/Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/data/raw/tmdb_movies_raw.csv"
TRANSFORMED_PATH = "/Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/data/transformed/tmdb_movies_transformed.csv"

# Ensure output folder exists
os.makedirs("data/transformed", exist_ok=True)

def load_cleaned_data():
    # Read CSV normally first (no parse_dates)
    df = pd.read_csv(CLEANED_PATH)

    # Explicitly convert release_date with fixed format (OPTION A)
    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(
            df["release_date"],
            format="%Y-%m-%d",
            errors="coerce"
        )

    print("Loaded cleaned data shape:", df.shape)
    return df

def add_profit_column(df):
    if "budget" in df.columns and "revenue" in df.columns:
        df["profit"] = df["revenue"] - df["budget"]
        print("Added column: profit")
    return df

def add_release_year(df):
    if "release_date" in df.columns:
        df["release_year"] = df["release_date"].dt.year
        print("Added column: release_year")
    return df

def add_rating_category(df):
    if "vote_average" in df.columns:

        def classify_rating(score):
            if score >= 8:
                return "Excellent"
            elif score >= 6:
                return "Good"
            elif score >= 4:
                return "Average"
            else:
                return "Poor"

        df["rating_category"] = df["vote_average"].apply(classify_rating)
        print("Added column: rating_category")

    return df

def save_transformed(df):
    df.to_csv(TRANSFORMED_PATH, index=False)
    print("Saved transformed data to:", TRANSFORMED_PATH)

if __name__ == "__main__":
    df = load_cleaned_data()
    df = add_profit_column(df)
    df = add_release_year(df)
    df = add_rating_category(df)
    save_transformed(df)

    print(" DATA TRANSFORMATION COMPLETED!")

