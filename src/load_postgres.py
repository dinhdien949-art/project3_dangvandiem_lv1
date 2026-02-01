import os
import pandas as pd
from sqlalchemy import create_engine

TRANSFORMED_PATH = "/Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/data/transformed/tmdb_movies_transformed.csv"

# ======= EDIT THESE WITH YOUR DB INFO =======
DB_USER = "dinhdien"
DB_PASSWORD = "mypassword"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "dinhdien"
TABLE_NAME = "movies"
# ============================================

def load_to_postgres():
    print("Loading data to PostgreSQL...")

    # Read transformed data
    df = pd.read_csv(TRANSFORMED_PATH)

    # Create connection string
    connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)

    # Load to PostgreSQL (replace table if exists)
    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="replace",
        index=False,
        chunksize=500
    )

    print(f"Successfully loaded data to table: {TABLE_NAME}")

if __name__ == "__main__":
    load_to_postgres()
