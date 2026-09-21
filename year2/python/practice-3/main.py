total_checks = 0
total_sales = 0.0
total_returns = 0.0

print("Касова зміна розпочата. Вводьте суми чеків або 'close' для завершення.")

while True:
    user_input = input("Введіть суму чека: ")

    if user_input.lower() == "close":
        break

    try:
        amount = float(user_input)
    except ValueError:
        print("Помилка: введіть коректне число або 'close'!")
        continue

    if amount == 0:
        print("Помилковий чек (сума 0), пропускаємо.")
        continue

    total_checks += 1

    if amount > 0:
        total_sales += amount
    else:
        total_returns += amount

balance = total_sales + total_returns

print("\n" + "=" * 30)
print("ПІДСУМКОВИЙ ЗВІТ ЗА ЗМІНУ")
print("=" * 30)
print(f"Загальна кількість чеків: {total_checks}")
print(f"Сума оплат (продажі): {total_sales:.2f} грн")
print(f"Сума повернень: {abs(total_returns):.2f} грн")
print(f"Баланс каси: {balance:.2f} грн")