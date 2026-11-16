from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers
from pathlib import Path

def main():
    data_path = Path(__file__).resolve().parent / "data" / "measurements.txt"
    print("Текущая директория", Path.cwd())
    if data_path.exists():
        print("Файл найден", data_path)
        numbers = read_numbers(data_path)
        print("Measurements:", numbers)
        print("Average:", calculate_average(numbers))
        print("Minimum:", find_min(numbers))
        print("Maximum:", find_max(numbers))
    else:
        print("файл не найден",data_path)

    logs_path = Path("logs")
    logs_path.mkdir(exist_ok=True)


if __name__ == "__main__":
    main()
