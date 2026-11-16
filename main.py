from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_max, find_min


def main():
    data_path = Path(__file__).resolve().parent / "data" / "measurements.txt"
    try:
        numbers = read_numbers(data_path)
        validate_numbers(numbers)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {data_path}")
        return
    except ValueError as error:
        print(f"Ошибка данных: {error}")
        return

    print("Измерения:", numbers)
    print("Среднее:", calculate_average(numbers))
    print("Минимум:", find_min(numbers))
    print("Максимум:", find_max(numbers))


if __name__ == "__main__":
    main()
