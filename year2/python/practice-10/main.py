import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
CODES = ("USD", "EUR", "AUD")


def get_exchange_data() -> list[dict]:
    """Get exchange rates data from NBU API."""
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code != 200:
            raise RuntimeError(f"Response code not 200 from NBU API: {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        raise RuntimeError("Error getting exchange rates from NBU API.") from e


def get_currency_items(data: list[dict], codes: tuple[str, ...]) -> list[dict]:
    """Filter exchange rate items by currency codes."""
    return (item for item in data if item.get("cc") in codes)


if __name__ == "__main__":
    try:
        data = get_exchange_data()
        currencies = get_currency_items(data, CODES)

        print(f"{'Назва':<25} {'Код':<5} {'Курс (грн)':<12} {'Дата'}")
        print("-" * 55)

        for item in currencies:
            print(f"{item['txt']:<25} {item['cc']:<5} {item['rate']:<12} {item['exchangedate']}")
    except RuntimeError as e:
        print("Currency rate not available.", e)