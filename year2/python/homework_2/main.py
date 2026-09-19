
user_input = input("Введіть кількість спожитих кВт·год за місяць: ")

RATE_TIER_1 = 2.64  # до 100 квт/год
RATE_TIER_2 = 4.32  # від 101 до 300 квт/год
RATE_TIER_3 = 6.00  # понад 300 квт/год

try:
    kwh = float(user_input)
    if kwh < 0:
        print("Помилка: кількість квт/год не може бути від'ємною!")
        exit()
except ValueError:
    print("Помилка: введіть коректне числове значення!")
    exit()

total_cost = 0.0

if kwh <= 100:
    total_cost = kwh * RATE_TIER_1
elif kwh <= 300:
    total_cost = (100 * RATE_TIER_1) + ((kwh - 100) * RATE_TIER_2)
else:
    total_cost = (
        (100 * RATE_TIER_1) + (200 * RATE_TIER_2) + ((kwh - 300) * RATE_TIER_3)
    )

print(f"Спожито: {kwh:.2f} квт/год")
print(f"До сплати: {total_cost:.2f} грн")