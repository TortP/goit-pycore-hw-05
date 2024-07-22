def generator_numbers(text: str):
    words = text.split()  # Розбиваємо текст на слова
    for word in words:
        # Перевіряємо, чи є слово дійсним числом
        if word.replace('.', '', 1).isdigit() and word.count('.') <= 1:
            yield float(word)


def sum_profit(text: str, func):
    return sum(func(text))


# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
