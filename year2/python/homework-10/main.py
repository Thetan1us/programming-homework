import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


def get_usd_rate() -> float | None:
    """Return the NBU's current USD exchange rate, or None if unavailable."""
    try:
        response = requests.get(URL, timeout=5)
    except requests.exceptions.RequestException as error:
        print(f"Не вдалося отримати курс валют: {error}")
        return None

    if response.status_code != 200:
        print(f"НБУ повернув помилку сервера (HTTP {response.status_code}).")
        return None

    data = response.json()
    for item in data:
        if item.get("cc") == "USD":
            return float(item["rate"])

    print("Курс USD відсутній у відповіді НБУ.")
    return None


if __name__ == "__main__":
    usd_rate = get_usd_rate()
    if usd_rate is not None:
        amount_uah = 250 * usd_rate
        print(f"$250 коштують {amount_uah:.2f} грн (курс: {usd_rate:.2f} грн за $1).")