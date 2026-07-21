import os
import sqlite3

PASSWORD = "admin123"      # Security Hotspot (hardcoded credential)


def duplicate_code_one():
    for i in range(100):
        if i % 2 == 0:
            print(i)


def duplicate_code_two():
    for i in range(100):
        if i % 2 == 0:
            print(i)


def calculate_average(numbers):
    total = 0

    for n in numbers:
        total += n

    unused_variable = "I am never used"    # Code Smell

    return total / len(numbers)


def divide(a, b):
    try:
        return a / b
    except:
        pass                 # Empty except block


def read_file():
    f = open("sample.txt", "r")   # Resource not closed
    print(f.read())


def inefficient_string():
    text = ""

    for i in range(1000):
        text += str(i)      # Inefficient string concatenation

    return text


def database():
    conn = sqlite3.connect("demo.db")   # Connection never closed

    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS employee(id INTEGER)"
    )

    print("Database Created")


def nested_conditions(x):

    if x > 0:

        if x < 100:

            if x % 2 == 0:

                if x > 50:

                    print("Complex logic")


def dangerous_command(command):
    os.system(command)      # Security Hotspot


def main():

    numbers = []

    # Possible ZeroDivisionError
    print(calculate_average(numbers))

    divide(10, 0)

    duplicate_code_one()

    duplicate_code_two()

    inefficient_string()

    read_file()

    database()

    dangerous_command("dir")


if __name__ == "__main__":
    main()
