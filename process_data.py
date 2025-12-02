import csv
import os

DATA_DIR = "./data"
OUTPUT_FILE = "processed_data.csv"

with open(OUTPUT_FILE, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["sales", "date", "region"])

    for filename in os.listdir(DATA_DIR):
        if not filename.endswith(".csv"):
            continue

        with open(os.path.join(DATA_DIR, filename), "r") as f:
            reader = csv.reader(f)

            # Skip header
            next(reader, None)

            for row in reader:
                # Skip corrupted or incomplete rows
                if len(row) < 5:
                    continue

                product, price_raw, qty_raw, date, region = row

                if product.strip().lower() == "pink morsel":
                    try:
                        # Clean price → remove $ and convert to float
                        price = float(price_raw.replace("$", "").strip())

                        qty = int(qty_raw.strip())

                        sale_value = price * qty

                        writer.writerow([sale_value, date, region])

                    except:
                        # Skip bad rows
                        continue
