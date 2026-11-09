import re


def normalize_ua_phone(raw_phone: str) -> str | None:
    try:
        digits = re.sub(r"\D", "", raw_phone)

        if len(digits) == 10 and digits.startswith("0"):
            return "+38" + digits
        elif len(digits) == 12 and digits.startswith("380"):
            return "+" + digits
        else:
            return None
    except Exception:
        return None


test_phones = [
    "+38(050)123-45-67",
    "050 123 45 67",
    "380501234567",
    "050-123-4567",
    "тел: 0501234567",
    "невідомо",
    "12345",
]

for phone in test_phones:
    print(f"{phone!r:25} -> {normalize_ua_phone(phone)}")
