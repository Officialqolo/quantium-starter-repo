import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_sales_data.csv"

# open the output file
with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)

    # add a csv header
    writer.writerow(["sales", "date", "region"])

    # go through all CSV files in the data folder
    for file_name in os.listdir(DATA_DIRECTORY):
        if not file_name.endswith(".csv"):
            continue  # skip non‑CSV files

        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)

            row_index = 0
            for row in reader:

                # skip header rows AND skip broken rows
                if row_index == 0 or len(row) < 5:
                    row_index += 1
                    continue

                product, raw_price, qty, date, region = row

                # we ONLY want "pink morsel"
                if product.lower() == "pink morsel":
                    price = float(raw_price.replace("$", ""))
                    sale_amount = price * int(qty)

                    writer.writerow([sale_amount, date, region])

                row_index += 1

print("DONE — formatted_sales_data.csv created successfully!")
