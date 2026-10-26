import pytest

from src.calculator import calculate_discount, divide


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_calculate_discount():
    assert calculate_discount(100, 20) == 80


def test_full_discount():
    assert calculate_discount(100, 100) == 0
