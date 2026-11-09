import csv
import json

orders = []

try:
    with open("data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "1":
                row["price"] = float(row["price"])
                row["quantity"] = int(row["quantity"])

                row["total_cost"] = row["price"] * row["quantity"]
                
                orders.append(row)
except (FileNotFoundError | PermissionError | IOError) as e:
    print(e)
except csv.Error as e:
    print(e)

try:
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(orders, file, ensure_ascii=False)
        print("The JSON file has been created")
except (FileNotFoundError | PermissionError | IOError) as e:
    print(e)
except json.decoder.JSONDecodeError as e:
    print(e)
