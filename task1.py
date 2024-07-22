def caching_fibonacci():
    cache = {}  # Створюємо словник для кешування

    def fibonacci(n):
        if n <= 1:
            return n
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Приклад використання:
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
