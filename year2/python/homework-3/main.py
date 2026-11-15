stop = False
parts_amount = 0
total_weight = 0
average_weight = 0
max_weight = None

print("Система контролю якості виробництва. Вводьте вагу деталей у грамах або 'stop' для завершення роботи програми \n")

while stop is False:
    user_input = input("Введіть вагу деталі: ").strip()

    if user_input.lower() == "stop":
        break

    try:
        weight = float(user_input)
    except ValueError:
        print("Введено нечислове значення, спробуйте знову!")
        continue

    if weight < 10 or weight > 1000:
        print(f"Увага! Брак сенсора або деталі. Вага {weight} г поза допустимим діапазоном (10-1000г). Деталь проігноровано.")
        continue
    
    parts_amount += 1
    total_weight += weight

    if max_weight is None or weight > max_weight:
        max_weight = weight

print("\nЗвіт контролю якості партії:")
print("загальна кількість прийнятих деталей - " + str(parts_amount) + " шт")
print("загальна вага партії - " + str(total_weight) + " г")

if parts_amount > 0:
    average_weight = total_weight / parts_amount
    print("середня вага однієї деталі - " + str(average_weight) + " г")
else:
    print("жодної коректної деталі не було прийнято")

if max_weight is not None:
    print("найважча деталь - " + str(max_weight) + " г")
else:
    print("не було знайдено найважчої деталі")