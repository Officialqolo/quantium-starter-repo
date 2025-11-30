import pandas as pd
from pathlib import Path

# Folder containing the CSV files
data_path = Path("data")

# Load all CSVs
files = [
    data_path / "daily_sales_data_0.csv",
    data_path / "daily_sales_data_1.csv",
    data_path / "daily_sales_data_2.csv",
]

# Read and combine
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Create Sales column: quantity * price
df["Sales"] = df["quantity"] * df["price"]

# Select only the required columns
final_df = df[["Sales", "date", "region"]]

# Save output
output_path = Path("processed_data.csv")
final_df.to_csv(output_path, index=False)

print(f"Done! File saved to {output_path.resolve()}")
# Task 2: Process sales data to extract Pink Morsels sales information