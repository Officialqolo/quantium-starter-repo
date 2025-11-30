import pandas as pd
import glob

# Load all three CSV files
files = glob.glob("data/daily_sales_data_*.csv")

dfs = []

for file in files:
    df = pd.read_csv(file)
    # Keep ONLY Pink Morsels
    df = df[df["product"] == "pink morsel"]
    # Calculate sales
    df["sales"] = df["quantity"] * df["price"]
    # Keep only required columns
    df = df[["sales", "date", "region"]]
    dfs.append(df)

# Combine all into one DataFrame
final_df = pd.concat(dfs, ignore_index=True)

# Save to output file
final_df.to_csv("data/formatted_sales_data.csv", index=False)

print("DONE — formatted_sales_data.csv created!")
