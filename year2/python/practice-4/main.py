def convert_to_meters(value: float, unit: str = "cm") -> float | None:
    """
    Переводить значення довжини у метри.

    Підтримує одиниці: cm, mm, inch.
    Якщо значення від'ємне або одиниця невідома - повертає None.
    """
    if value < 0:
        print("Значення має бути більшим за 0.")
        return None

    if unit == "cm" or unit == "см":
        return value * 0.01
    elif unit == "mm" or unit == "мм":
        return value * 0.001
    elif unit == "inch" or unit == "дюйм":
        return value * 0.0254
        
    print("Невідома одиниця.")
    return None

def calculate_bmi(weight_kg: float, height_m: float) -> tuple[float, str] | None:
    """
    Рахує індекс маси тіла (BMI) за формулою weight / (height ** 2).

    Повертає кортеж (округлений BMI, категорія).
    Якщо вага або зріст <= 0 — повертає None.
    """
    if weight_kg <= 0 or height_m <= 0:
        print("Вага і зріст не можуть бути 0 або меншим за 0.")
        return None

    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi <= 24.9:
        category = "Normal"
    elif bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    return bmi, category

value_1 = convert_to_meters(float(input("Введіть значення довжини: ")), input("Введіть одиницю вимірювання: "))
if value_1 is not None:
    print(str(value_1) + "м")

value_2 = calculate_bmi(float(input("Введіть Вашу вагу в кг: ")), float(input("Введіть Ваш зріст в м: ")))
if value_2 is not None:
    print(value_2)