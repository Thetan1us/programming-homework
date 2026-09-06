cargo_weight = float(input("Введіть вагу, яку треба перевезти в кг: "))
distance = float(input("Введіть відстань перевезення в км: "))
price = float(input("Введіть вартість вантажу в грн: "))

base_fare = 100
weight_rate = 20
distance_rate = 15

delivery_cost = base_fare + (cargo_weight * weight_rate) + (distance * distance_rate)

print(f"Фінальна вартість доставки - {delivery_cost:.2f} грн")