# Cursor, Python и Git: учебный проект

Проект содержит простой пример Python-программы, которая выводит приветствие, и скрипт для чтения CSV-файла со стандартной библиотекой `csv`. В `data.csv` приведены пять строк данных. Файл `setup_versions.txt` фиксирует версии Cursor, Python и Git.

## Запуск

В PowerShell из папки проекта создайте виртуальное окружение и запускайте примеры так:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe .\hello.py
.\.venv\Scripts\python.exe .\read_csv.py .\data.csv
```

Скриншот успешного чтения CSV находится в `read_csv_success_clean.png`.
