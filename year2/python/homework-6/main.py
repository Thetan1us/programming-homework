inventory = [
    {"item": "Ноутбук", "supplier": "TechCorp", "qty": 10, "price": 25000.0},
    {"item": "Мишка", "supplier": "AccsCo", "qty": 50, "price": 450.0},
    {"item": "Клавіатура", "supplier": "TechCorp", "qty": 20, "price": 1200.0},
    {"item": "Монітор", "supplier": "ScreenMaster", "qty": 8, "price": 8500.0},
    {"item": "Ноутбук", "supplier": "MegaDist", "qty": 5, "price": 26000.0},
]


def analyze_inventory(items):
    unique_suppliers = set()
    total_stock = {}
    total_warehouse_value = 0.0

    for entry in items:
        item_name = entry["item"]
        supplier = entry["supplier"]
        quantity = entry["qty"]
        price = entry["price"]

        unique_suppliers.add(supplier)
        total_stock[item_name] = total_stock.get(item_name, 0) + quantity
        total_warehouse_value += quantity * price

    return unique_suppliers, total_stock, total_warehouse_value


def main():
    unique_suppliers, total_stock, total_warehouse_value = analyze_inventory(inventory)

    print("Унікальні постачальники:", unique_suppliers)
    print("Загальна кількість за товарами:", total_stock)
    print("Загальна вартість складу:", total_warehouse_value)


if __name__ == "__main__":
    main()