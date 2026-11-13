import functools
import pytest


def validate_positive_numbers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)):
                if arg <= 0:
                    raise ValueError(
                        "Аргументи повинні бути суворо додатними числами"
                    )

        return func(*args, **kwargs)

    return wrapper


@validate_positive_numbers
def get_area(a, b):
    return a * b + 1


if __name__ == "__main__":
    print("Площа (5, 10):", get_area(5, 10))

    #try:
    #    print("Площа (-3, 4):", get_area(-3, 4))
    #except ValueError as e:
    #    print("Виявлено помилку:", e)

    assert get_area(3, 4) == 12, f"Expected 12 for get_area(3,4), got {get_area(3,4)}"
    with pytest.raises(ValueError):
        get_area(-3, 4)