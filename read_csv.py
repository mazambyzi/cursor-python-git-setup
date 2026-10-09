# read_csv.py
import csv
import sys
from pathlib import Path


def main():
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data.csv")
    if not csv_path.is_file():
        raise SystemExit(f"CSV file not found: {csv_path}\nUsage: python read_csv.py path/to/file.csv")

    with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    # Ручная правка без ИИ: перевёл подписи и выровнял отступ.
    print(f"File: {csv_path}")
    print(f"Количество строк: {len(rows)}")
    print(f"Столбцы: {', '.join(reader.fieldnames or [])}")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
