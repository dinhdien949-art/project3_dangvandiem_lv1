#from src.extract_data import extract_data_from_url

#URL = "https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv"
#OUTPUT_PATH = "../data/raw/tmdb_movies_raw.csv"

#if __name__ == "__main__":
 #   extract_data_from_url(URL, OUTPUT_PATH)

from src.extract_data import extract_data_from_url
import subprocess
import sys
import time

URL = "https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv"
RAW_PATH = "data/raw/tmdb_movies_raw.csv"


def run_step(name, command):
    print(f"\n========== {name} ==========")
    start = time.time()

    result = subprocess.run(command, shell=True)

    elapsed = round(time.time() - start, 2)

    if result.returncode != 0:
        print(f" {name} FAILED after {elapsed} seconds")
        sys.exit(1)
    else:
        print(f" {name} COMPLETED in {elapsed} seconds")


if __name__ == "__main__":

    print("\n🚀 STARTING FULL ETL + ANALYSIS PIPELINE...\n")

    # ===== STEP 1: EXTRACT (kept as your original style) =====
    print("========== STEP 1 - EXTRACT DATA ==========")
    extract_data_from_url(URL, RAW_PATH)

    # ===== STEP 2: VALIDATE =====
    run_step(
        "STEP 2 - VALIDATE DATA",
        "python /Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/src/validate.py"
    )
    # ===== STEP 3: CLEAN =====
    run_step(
        "STEP 3 - CLEAN DATA",
        "python /Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/src/clean.py"
    )

    # ===== STEP 4: TRANSFORM =====
    run_step(
        "STEP 4 - TRANSFORM DATA",
        "python /Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/src/transform.py"
    )

    # ===== STEP 5: LOAD TO POSTGRES =====
    run_step(
        "STEP 5 - LOAD TO POSTGRESQL",
        "python /Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/src/load_postgres.py"
    )

    # ===== STEP 6: ANALYSIS WITH PANDAS =====
    run_step(
        "STEP 6 - ANALYSIS (PANDAS)",
        "python /Users/dinhdien/PycharmProjects/PythonProject/project3_dangvandiem/src/analysis.py"
    )

    print("\n PIPELINE COMPLETED SUCCESSFULLY!")

