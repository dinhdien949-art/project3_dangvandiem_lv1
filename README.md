# Project 3 — ETL Pipeline with Pandas & PostgreSQL

##  Overview

This project implements an **ETL (Extract – Transform – Load) pipeline** using Python and Pandas to process the **TMDB Movies Dataset** and store the cleaned data into a PostgreSQL database.

The pipeline follows a modular structure, where each step of the ETL process is handled by a separate script for better maintainability, testing, and scalability.

---

##  Project Objectives

This project aims to:

- Extract movie data from a public dataset (CSV hosted online)
- Clean and validate the data
- Transform it into a structured format suitable for analysis
- Load the processed data into a PostgreSQL database
- Provide a reproducible and well-organized ETL workflow

---

##  Project Structure
project3_dangvandiem/
│
├── data/ # Raw and processed data (ignored by Git)
├── sql/
│ └── create_tables.sql # SQL script to create PostgreSQL tables
│
├── src/
│ ├── extract_data.py # Extract data from URL
│ ├── clean.py # Data cleaning logic
│ ├── transform.py # Data transformation logic
│ ├── validate.py # Data validation checks
│ ├── load_postgres.py # Load data into PostgreSQL
│ ├── analysis.py # Optional analysis step
│ └── main.py # Orchestrates the ETL pipeline
│
├── .gitignore # Git ignore file
└── README.md # Project documentation

---

##  Technologies Used

- Python 3.x  
- Pandas  
- PostgreSQL  
- psycopg2 (PostgreSQL connector)  
- Requests / Pandas (for fetching CSV from URL)  

## Run the ETL Pipeline

python src/main.py
This will:

Download the dataset
Clean and transform the data
Validate the results
Load the processed data into PostgreSQL
Analysis the questions of project3. 


