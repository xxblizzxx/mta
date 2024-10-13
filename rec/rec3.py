def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Приклад використання
print(fibonacci(2))  # Виведе: 1
print(fibonacci(3))  # Виведе: 2
print(fibonacci(4))  # Виведе: 3
