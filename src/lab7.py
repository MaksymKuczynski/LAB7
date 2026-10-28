"""
Лабораторна робота № 7: Читання та запис даних у файли
Варіант 13: Робота з CSV файлом співробітників (employees.csv)
"""

import os
import csv

# Демонстраційний блок з шаблону (src/input.txt)
try:
    with open("src/input.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Вміст файлу src/input.txt:")
        print(content)
except FileNotFoundError:
    print("Помилка: Файл 'src/input.txt' не знайдено!")
    with open("src/input.txt", "w", encoding="utf-8") as file:
        file.write("Це демонстраційний вміст файлу input.txt.")
    print("Створено новий файл 'src/input.txt'.")
except IOError as e:
    print(f"Помилка читання файлу: {e}")

print("\n" + "="*30 + "\n")

# Створення або перезапис CSV файлу src/employees.csv, якщо його немає або він порожній
if not os.path.exists("src/employees.csv") or os.path.getsize("src/employees.csv") == 0:
    try:
        with open("src/employees.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Прізвище", "Ім’я", "Посада", "Зарплата"])
            writer.writerow(["Тадеуш", "Костюшко", "Розробник", "45000"])
            writer.writerow(["Новак", "Марек", "Дизайнер", "38000"])
            writer.writerow(["Дуда", "Анджей", "СЕО", "80000"])
            writer.writerow(["Шевченко", "Олена", "Тестувальник", "32000"])
            writer.writerow(["Мельник", "Андрій", "Розробник", "40000"])
        print("Створено файл 'src/employees.csv' з даними.")
    except IOError as e:
        print(f"Помилка створення файлу: {e}")

# Читання файлу src/employees.csv та вивід у вигляді таблиці
print("Таблиця співробітників:")
try:
    with open("src/employees.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # перевірка, щоб рядок не був порожнім
                print(f"{row[0]:<16} {row[1]:<12} {row[2]:<15} {row[3]:<10}")
except FileNotFoundError:
    print("Помилка: Файл src/employees.csv не знайдено!")
except IOError as e:
    print(f"Помилка читання: {e}")

print("\n" + "="*30 + "\n")

# Запитання про посаду людини та запис у src/employees_by_position.txt
target_position = input("Введіть посаду для фільтрації (наприклад, Розробник): ").strip()

try:
    with open("src/employees.csv", "r", encoding="utf-8") as infile, \
         open("src/employees_by_position.txt", "w", encoding="utf-8", newline="") as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            if row and (row[2].lower() == target_position.lower() or row[3] == "Зарплата"):
                writer.writerow(row)
                
    print(f"Результати записано у файл 'src/employees_by_position.txt'.")
except FileNotFoundError:
    print("Файл src/employees.csv не знайдено!")
except IOError as e:
    print(f"Помилка при роботі з файлом: {e}")

print("\n" + "="*30 + "\n")

# Пошук співробітника з найвищою зарплатою
filename = input("Введіть ім'я файлу для пошуку (наприклад, src/employees.csv): ").strip()

try:
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader) # Пропускаємо заголовок
        
        max_salary = -1
        best_employee = None
        
        for row in reader:
            if row:
                salary = float(row[3])
                if salary > max_salary:
                    max_salary = salary
                    best_employee = row
                
        if best_employee:
            print(f"\nНайвища зарплата у файлі '{filename}':")
            print(f"Працівник: {best_employee[0]} {best_employee[1]}, Посада: {best_employee[2]}, Зарплата: {best_employee[3]}")
            
except FileNotFoundError:
    print(f"Помилка: Файл '{filename}' не знайдено!")
except ValueError:
    print("Помилка: Некоректний формат числа (зарплати) у файлі!")
except IOError as e:
    print(f"Помилка введення-виведення: {e}")