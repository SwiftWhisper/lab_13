import csv
import json

# Вихідні дані
alfavit = {
    "Алфавіт": [
        {"Буква алфавіту": "А", "Порядковий номер": 1, "Голосна чи приголосна?": "Голосна"},
        {"Буква алфавіту": "Б", "Порядковий номер": 2, "Голосна чи приголосна?": "Приголосна"},
        {"Буква алфавіту": "В", "Порядковий номер": 3, "Голосна чи приголосна?": "Приголосна"},
        {"Буква алфавіту": "Г", "Порядковий номер": 4, "Голосна чи приголосна?": "Приголосна"},
    ]
}

csv_file = "data.csv"
json_file = "data.json"


# Функція для створення CSV файлу
def create_csv(data, csv_file):
    try:
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["Буква алфавіту", "Порядковий номер", "Голосна чи приголосна?"],
            )
            writer.writeheader()
            writer.writerows(data["Алфавіт"])
        print(f"Дані успішно записані в {csv_file}")
    except Exception as e:
        print(f"Помилка при записі в CSV файл: {e}")


# Функція для додавання нової букви в JSON
def add_letter_to_json(key, num, insh, json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Перевірка, чи буква вже є в JSON файлі
        if any(item["Буква алфавіту"] == key for item in data["Алфавіт"]):
            print(f"Буква '{key}' вже існує в JSON файлі.")
        else:
            # Додаємо нову букву
            new_letter = {
                "Буква алфавіту": key,
                "Порядковий номер": num,
                "Голосна чи приголосна?": insh,
            }
            data["Алфавіт"].append(new_letter)

            with open(json_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Буква '{key}' успішно додана.")
    except FileNotFoundError:
        print(f"Помилка: файл {json_file} не знайдено.")
    except Exception as e:
        print(f"Помилка при додаванні букви в JSON файл: {e}")


# Функція для конвертації JSON у CSV з додаванням нових рядків
def json_to_csv_with_new_rows(json_file, csv_file, new_rows):
    try:
        # Читаємо існуючі дані з JSON файлу
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Додаємо нові записи
        data["Алфавіт"].extend(new_rows)

        # Записуємо всі дані в CSV файл
        create_csv(data, csv_file)
        print(f"Дані з JSON успішно записані в {csv_file} з додаванням нових рядків.")
    except FileNotFoundError:
        print(f"Помилка: файл {json_file} не знайдено.")
    except Exception as e:
        print(f"Помилка при конвертації JSON у CSV: {e}")


# Основне меню
def main():
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(alfavit, file, ensure_ascii=False, indent=4)

    create_csv(alfavit, csv_file)

    while True:
        print("\nМеню:")
        print("1. Конвертувати з JSON у CSV з додаванням нових рядків")
        print("2. Додати букву в JSON файл")
        print("3. Вийти")

        choice = input("Виберіть опцію (1-3): ")

        if choice == "1":
            # Нові рядки для додавання
            new_rows = [
                {"Буква алфавіту": "Д", "Порядковий номер": 5, "Голосна чи приголосна?": "Приголосна"},
                {"Буква алфавіту": "Е", "Порядковий номер": 6, "Голосна чи приголосна?": "Голосна"},
            ]
            json_to_csv_with_new_rows(json_file, csv_file, new_rows)
        elif choice == "2":
            key = input("Введіть нову букву: ")
            num = input("Введіть порядковий номер букви: ")
            try:
                num = int(num)
            except ValueError:
                print("Порядковий номер повинен бути числом.")
                continue

            while True:
                print("Буква голосна чи приголосна? (1 - голосна; 2 - приголосна)")
                subCh = input()
                if subCh == "1":
                    insh = "Голосна"
                    break
                elif subCh == "2":
                    insh = "Приголосна"
                    break
                else:
                    print("Невірний вибір. Спробуйте ще раз.")

            add_letter_to_json(key, num, insh, json_file)
        elif choice == "3":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


main()
