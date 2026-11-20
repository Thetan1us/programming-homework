class BankAccount:
    """Банківський рахунок з контролем балансу та історією операцій."""

    def __init__(self, account_id: str, owner: str, initial_balance: float = 0.0) -> None:
        """Ініціалізує поля рахунку та початковий баланс."""

        self.account_id: str = account_id
        self.owner: str = owner
        self._history: list[float] = []
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        """Повертає поточний баланс."""

        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        """Перевіряє тип і позитивний баланс."""

        if not isinstance(value, (int, float)):
            raise TypeError("Баланс має бути числом.")
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним.")
        self._balance = float(value)



    def deposit(self, amount: float) -> None:
        """Поповнює рахунок та зберігає операцію в історії."""

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за 0.")
        self._balance += float(amount)
        self._history.append(float(amount))

    def withdraw(self, amount: float) -> None:
        """Знімає кошти з рахунку, якщо вистачає балансу."""

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума зняття має бути більшою за 0.")
        if amount > self._balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self._balance -= float(amount)
        self._history.append(float(-amount))

    def __str__(self) -> str:
        """Повертає текстовий опис рахунку."""

        return (f"Рахунок {self.account_id}, власник: {self.owner}, баланс: {self.balance:.2f} грн.")

    def __len__(self) -> int:
        """Повертає кількість проведених транзакцій."""

        return len(self._history)

    def __eq__(self, other: object) -> bool:
        """Порівнює два рахунки за account_id."""

        if not isinstance(other, BankAccount):
            raise TypeError("Обрано неправильний об'єкт для порівняння")
        return self.account_id == other.account_id


if __name__ == "__main__":
    acc1 = BankAccount("01", "Нікіта Горбенко", 1000.0)
    acc2 = BankAccount("01", "Нікіта Горбенко")
    acc3 = BankAccount("02", "Іван Іваненко", 500.0)

    print(acc1)
    acc1.deposit(250)
    acc1.withdraw(400)
    print(acc1)
    print("Кількість транзакцій:", len(acc1))
    print("acc1 == acc2:", acc1 == acc2)
    print("acc1 == acc3:", acc1 == acc3)

    try:
        acc1.balance = -50
    except ValueError as err:
        print("Помилка встановлення балансу:", err)

    try:
        acc1.deposit(-100)
    except ValueError as err:
        print("Помилка поповнення:", err)

    try:
        acc1.withdraw(5000)
    except ValueError as err:
        print("Помилка зняття:", err)