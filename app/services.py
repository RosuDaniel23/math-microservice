def factorial(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    return 1 if n == 0 else n * factorial(n - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def power(n):
    return n ** 2
