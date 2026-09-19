balance = int(input("Поточний баланс картки (грн): "))
payment = int(input("Сума платежу (грн): "))

if payment <= 0:
    raise SystemExit("Сума має бути більшою за 0")

category = int(input("Категорія акаунту (\"1\": standard, \"2\": gold, \"3\": platinum): "))

if category < 1 or category > 3:
    raise SystemExit("Невідома категорія")

commission = None

if category == 1:
    commission = 0.02
if category == 2:
    commission = 0.01
if category == 3:
    commission = 0

if (payment + payment * commission > balance):
    raise SystemExit("Недостатньо коштів")

balance -= payment + (payment * commission)
print("Залишок після виконання операції - " + str(balance) + " грн")
