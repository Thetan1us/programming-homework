import re


def parse_order_message(raw_message):
    cleaned_message = raw_message.strip()
    pattern = r"ID_(\d+)\s+Promo:\s*(\S+)\s+Sum:\s*(\d+(?:\.\d+)?)\s*UAH"
    match = re.search(pattern, cleaned_message)

    if match is None:
        return None

    order_id = int(match.group(1))
    promo_code = match.group(2)
    order_sum = float(match.group(3))

    return order_id, promo_code, order_sum


def main():
    raw_message = " [ORDER]: ID_84920 Promo: SUMMER2026 Sum: 1250.00UAH Status: PAID "
    parsed_order = parse_order_message(raw_message)

    if parsed_order is None:
        print("Формат повідомлення не підтримується")
        return

    order_id, promo_code, order_sum = parsed_order
    print(f"Order ID: {order_id}")
    print(f"Promo code: {promo_code}")
    print(f"Order sum: {order_sum}")


if __name__ == "__main__":
    main()