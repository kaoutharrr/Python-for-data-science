def square(x: int | float) -> int | float:
    """sqaure of x"""
    return x*x

def pow(x: int | float) -> int | float:
    """power of x"""
    return x**x

def outer(x: int | float, function) -> object:
    """Return a closure that applies function repeatedly to x."""
#     count = 0
# def inner() -> float