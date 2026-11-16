def calculate_discount(order_amount: float, client_status: str) -> float | None:
    """
    order_amount - число з плаваючою комою, вартість замовлення;
    client_status - рядок, статус клієнта (new, silver, gold)
    """

    right_status = client_status == "new" or client_status == "silver" or client_status == "gold"

    if order_amount <= 0 or not right_status:
         print("Неправильно введено вартість замовлення або статус клієнта")
         return None

    discount = 0.0
    match client_status:
        case "silver":
            discount = 0.05
        case "gold":
            discount = 0.1
    
    if order_amount > 10000:
        discount += 0.02

    return discount

def get_final_price(order_amount: float, discount_amount: float) -> float:
    if order_amount <= 0 or not isinstance(order_amount, float) or discount_amount <= 0 or not isinstance(discount_amount, float):
        print("Неправильно введено вартість замовлення чи знижку")
    
    return order_amount - (order_amount * discount_amount)

price = float(input("Введіть вартість замовлення: "))
status = input("Введіть статус клієнта: ").lower()

discount = calculate_discount(price, status)

if not discount is None:
    print(f"Фінальна вартість для клієнта {status} - {get_final_price(price, discount)} грн")
else:
    print("Знайдено помилку в оформленні замовлення. Програму буде завершено.")