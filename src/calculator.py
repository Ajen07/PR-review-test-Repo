def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_discount(price: float, percentage: float) -> float:
    """Return the price after applying a percentage discount."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100")

    return price * (1 - percentage / 100)
