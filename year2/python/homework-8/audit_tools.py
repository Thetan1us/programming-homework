from functools import wraps


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Виклик {func.__name__} з аргументами: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log_execution
def calc_vat(amount: float, vat_rate: float = 0.20) -> float:
    if amount < 0:
        raise ValueError("Сума не може бути від'ємною")
    return amount * vat_rate