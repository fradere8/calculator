def add_numbers(a: float, b: float) -> float:
    """Складывает два числа и возвращает результат."""
    return a + b


def divide(a,  b):
    if b == 0:
        return "Нельзя делить на ноль"
    else:
        return a / b


p = divide(1, 0)
print(p)

a = add_numbers(1, 2)
b = add_numbers(3, 4)
c = add_numbers(5, 6)
print(a, b, c)