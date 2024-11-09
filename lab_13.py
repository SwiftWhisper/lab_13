import csv
import json

alfavit = [
    {"Буква алфавіту": "А", "Порядковий номер": 1, "Голосна чи приголосна?": "Голосна"},
    {
        "Буква алфавіту": "Б",
        "Порядковий номер": 2,
        "Голосна чи приголосна?": "Приголосна",
    },
    {
        "Буква алфавіту": "В",
        "Порядковий номер": 3,
        "Голосна чи приголосна?": "Приголосна",
    },
    {
        "Буква алфавіту": "Г",
        "Порядковий номер": 4,
        "Голосна чи приголосна?": "Приголосна",
    },
]

csv_file = "data.csv"
json_file = "data.json"


# Функція для створення csv файлу
def create_csv(data, csv_file):
    try:
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Буква алфавіту",
                    "Порядковий номер",
                    "Голосна чи приголосна?",
                ],
            )
            writer.writeheader()
            writer.writerows(data)
        print(f"Дані успішно записані в {csv_file}")
    except Exception as e:
        print(f"Помилка при записі в CSV файл: {e}")


# Функція для конвертування даних з CSV у JSON
def csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        with open(json_file, mode="w", encoding="utf-8") as json_f:
            json.dump(rows, json_f, indent=4, ensure_ascii=False)

        print(f"Дані успішно переписані в {json_file}")
    except FileNotFoundError:
        print(f"Помилка: файл {csv_file} не знайдено.")
    except Exception as e:
        print(f"Помилка при переписуванні даних з CSV в JSON: {e}")


# Функція для додавання букви в JSON
def add_letter_to_json(key, num, insh, json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Перевірка, чи буква вже є в JSON файлі
        if any(item["Буква алфавіту"] == key for item in data):
            print(f"Буква '{key}' вже існує в JSON файлі.")
        else:
            # Додаємо нову букву
            new_letter = {
                "Буква алфавіту": key,
                "Порядковий номер": num,
                "Голосна чи приголосна?": insh,
            }
            data.append(new_letter)

            with open(json_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Буква '{key}' успішно додана.")
    except FileNotFoundError:
        print(f"Помилка: файл {json_file} не знайдено.")
    except Exception as e:
        print(f"Помилка при додаванні букви в JSON файл: {e}")


# Основне меню
def main():
    create_csv(alfavit, csv_file)

    while True:
        print("\nМеню:")
        print("1. Конвертувати з CSV в JSON")
        print("2. Додати букву в JSON файл")
        print("3. Вийти")

        choice = input("Виберіть опцію (1-3): ")

        if choice == "1":
            csv_to_json(csv_file, json_file)
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
