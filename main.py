import json
import logging
from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_max, find_min

PROJECT_DIR = Path(__file__).resolve().parent


def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


CONFIG = load_config(PROJECT_DIR / "config.json")
LOG_PATH = PROJECT_DIR / CONFIG["log_file"]
LOG_PATH.parent.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    logging.info("Запуск программы")
    data_path = PROJECT_DIR / CONFIG["input_file"]
    try:
        numbers = read_numbers(data_path)
        logging.info("Файл успешно прочитан: %s", data_path)
        logging.info("Количество прочитанных значений: %d", len(numbers))
        validate_numbers(numbers)
    except FileNotFoundError as error:
        logging.error("Файл не найден: %s", error.filename)
        print(f"Ошибка: файл не найден: {data_path}")
        return
    except ValueError as error:
        logging.error("Ошибка данных: %s", error)
        print(f"Ошибка данных: {error}")
        return
    else:
        print("Измерения:", numbers)
        print("Среднее:", calculate_average(numbers))
        print("Минимум:", find_min(numbers))
        print("Максимум:", find_max(numbers))
    finally:
        logging.info("Завершение программы")

if __name__ == "__main__":
    main()
