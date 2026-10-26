def divide(a: float, b: float) -> float:
    """Divide a by b."""
    return a / b


def calculate_discount(price: float, percentage: float) -> float:
    """Return the price after applying a percentage discount."""
    if price < 0:
        raise ValueError("Price cannot be negative")

    return price * (1 + percentage / 100)


def calculate_total(price: float, quantity: int) -> float:
    """Return the total price for a quantity of items."""
    return price + quantity
