class OrderItem:

    def __init__(self, title: str, price: float, quantity: int):
        self.title = title
        self.price = price
        self.quantity = quantity

    def get_cost(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return (
            f"Товар: {self.title} | {self.quantity} шт. "
            f"x {self.price:g} грн"
        )


class ShoppingCart:

    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self._items = []

    def add_item(self, item: OrderItem) -> None:
        self._items.append(item)

    def __len__(self) -> int:
        return len(self._items)

    def get_total_sum(self) -> float:
        return sum(item.get_cost() for item in self._items)


def print_receipt(cart: ShoppingCart) -> None:
    print(f"\nПідсумковий чек для {cart.customer_name}:")
    for item in cart._items:
        print(f"{item} = {item.get_cost():g} грн")
    print(f"Кількість товарів: {len(cart)}")
    print(f"До сплати: {cart.get_total_sum():g} грн")


def main():
    try:
        cart = ShoppingCart("Олена")
        cart.add_item(OrderItem("Мишка", 450.0, 2))
        cart.add_item(OrderItem("Клавіатура", 1200.0, 1))

        print(f"Товарів у кошику: {len(cart)}")
        print_receipt(cart)
    except (TypeError, ValueError) as error:
        print(f"Не вдалося створити замовлення: {error}")


if __name__ == "__main__":
    main()