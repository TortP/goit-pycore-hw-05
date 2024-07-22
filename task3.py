import sys


# Розбирає рядок логу на складові частини.
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }


def load_logs(file_path: str) -> list:  # Завантажує логи з файлу.
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


# Фільтрує логи за рівнем.
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]


# Підраховує кількість логів за кожним рівнем.
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        if level not in counts:
            counts[level] = 0
        counts[level] += 1
    return counts


# Виводить кількість логів за кожним рівнем.
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print('-' * 26)
    for level, count in counts.items():
        print(f"{level:<17} | {count:<8}")


def main():  # Головна функція програми.
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логів як аргумент командного рядка.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЛогів для рівня '{level}' не знайдено.")


if __name__ == "__main__":
    main()
