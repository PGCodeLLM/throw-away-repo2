"""Basic arithmetic helpers."""


def add(a, b):
    return a + b


def subtract(a, b):
    # BUG: this adds instead of subtracting
    return a + b


def divide(a, b):
    # BUG: no zero check
    return a / b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b
