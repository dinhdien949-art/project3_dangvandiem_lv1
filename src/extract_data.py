import pandas as pd
import os

def extract_data_from_url(url, output_path):
    data_frame = pd.read_csv(url)
    print("Extracting data....")
    print(f"Data extracted: {data_frame.shape[0]} rows, {data_frame.shape[1]} columns")

    # 🔧 Create folder if not exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    data_frame.to_csv(output_path, index=False)
    print(f" Data saved to {output_path}")


