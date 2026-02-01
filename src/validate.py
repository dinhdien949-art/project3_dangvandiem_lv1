import pandas as pd

RAW_PATH = "/Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/data/raw/tmdb_movies_raw.csv"

def load_raw_data():
    df = pd.read_csv(RAW_PATH)
    print("Number of data shape:", df.shape)
    return df

#Check duplicates

def check_duplicates(df):
    num_dup = df.duplicated().sum()
    print(f"Number of duplicate rows: {num_dup}")

#Check NULL values

def check_nulls(df):
    null_count = df.isnull().sum()
    null_percent = (null_count / len(df)) * 100

    null_summary = pd.DataFrame({
        "null_count": null_count,
        "null_percent": null_percent,
    })

    print("\n=== NULL SUMMARY ===")
    print(null_summary.sort_values(by="null_percent", ascending=False))

#Check numeric range validity (data quality rules)

def check_numeric_validatity(df):
    issues = {}

    if "budget"  in df.columns:
        issues["negative_budget"] = (df["budget"] < 0).sum()

    if "revenue" in df.columns:
        issues["negative_revenue"] = (df["revenue"] < 0).sum()

    if "vote_average" in df.columns:
        issues["invalid_vote"] = (~df["vote_average"].between(0, 10)).sum()

    print("\n=== DATA QUALITY ISSUES ===")
    for k, v in issues.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    df = load_raw_data()
    check_duplicates(df)
    check_nulls(df)
    check_numeric_validatity(df)

