def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


sequence = fibonacci(10)
for number in sequence:
    print(number)