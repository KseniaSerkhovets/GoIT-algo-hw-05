import argparse
import os

def parse_log_line(line: str) -> dict:
    try:
        parts = line.split(maxsplit=3)
        if len(parts) < 4:
            return None  # Якщо рядок не відповідає формату, повертаємо None
        date, time, level, message = parts
        log_line = {
            "date": date,
            "time": time,
            "level": level,
            "message": message.strip()
        }
        return log_line
    except Exception as e:
        print(f"Помилка при обробці логів: {e}")
        return None

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r") as fh:
            lines = [el for el in fh.readlines()]
        logs_list = []
        for line in lines:
            logs_list.append(parse_log_line(line))

        return logs_list
    except:
        print("Помилка при відкритті або читанні файлу")
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    filterd_logs = list(filter(lambda x: x["level"] == level, logs))
    return filterd_logs

def count_logs_by_level(logs: list) -> dict:
    
    level_count = {}
    for log_line in logs:
        if log_line is None:
            continue  # Пропускаємо `None` значення
        if log_line["level"] in level_count:
            level_count[log_line["level"]] += 1
        else:
            level_count[log_line["level"]] = 1
    return level_count


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for key, value in counts.items():
        print(f'{key:<16} | {value}')
    return


def main():
    parser = argparse.ArgumentParser(description="Аналізатор лог-файлів")
    parser.add_argument("file_path", help="Шлях до файлу логів")
    parser.add_argument("log_level", nargs="?", help="(Необов’язково) рівень логування", default=None)
    
    args = parser.parse_args()
    if not os.path.exists(args.file_path):
        print("Файл з даною назвою не існує")
        exit()

    # Завантажуємо логи
    logs = load_logs(args.file_path)

    if not logs:  # Якщо логи не були завантажені
        exit()
    
    # Відображаємо загальну статистику
    display_log_counts(count_logs_by_level(logs))

    # Якщо користувач вказав рівень логування – фільтруємо та виводимо деталі
    if args.log_level:
        level_logs = filter_logs_by_level(logs, args.log_level.upper())
        print(f"\nДеталі логів для рівня '{args.log_level.upper()}':")
        for log in level_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")



if __name__ == "__main__":
    main()

# python main.py log_file.txt
# python main.py log_file.txt ERROR
# python main.py loewu_frkgmile.txt