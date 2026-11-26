import numpy as np


def main():
    traffic = np.random.randint(50, 501, size=30)
    average_traffic = float(np.mean(traffic))

    peak_mask = traffic > average_traffic
    peak_days = int(np.sum(peak_mask))
    peak_traffic = traffic[peak_mask]

    marked_traffic = np.where(traffic > 450, -1, traffic)

    print(f"Середньодобовий трафік: {average_traffic:.2f} GB")
    print(f"Днів з піковим навантаженням: {peak_days}")
    print(f"Пікове навантаження: {peak_traffic}")
    print(f"Всі значення трафіку з урахуванням критичного перевантаження: {marked_traffic}")


if __name__ == "__main__":
    main()