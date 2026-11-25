import csv
import json


def create_sample_csv(filepath):
    rows = [
        {"id": "1", "name": "Нікіта Горбенко", "department": "DevOps", "salary": "999999"},
        {"id": "2", "name": "Андрій Мельник", "department": "QA", "salary": "28000"},
        {"id": "3", "name": "Ірина Бондар", "department": "Backend", "salary": "52000"},
        {"id": "4", "name": "Максим Ткаченко", "department": "Support", "salary": "22000"},
    ]

    with open(filepath, mode="w", encoding="utf-8", newline="") as csv_file:
        fieldnames = ["id", "name", "department", "salary"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def stream_high_earners(filepath: str, min_salary: float):
    with open(filepath, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            employee_salary = float(row["salary"])
            if employee_salary >= min_salary:
                yield {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "department": row["department"],
                    "salary": employee_salary,
                }


def main():
    csv_path = "./employees.csv"
    output_path = "./high_earners.json"
    min_salary = 35000.0

    create_sample_csv(csv_path)

    high_earners = []
    for employee in stream_high_earners(csv_path, min_salary):
        high_earners.append(employee)

    with open(output_path, mode="w", encoding="utf-8") as json_file:
        json.dump(high_earners, json_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()