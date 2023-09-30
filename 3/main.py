from infix import to_infix

input_strings = [
    "+ - 13 4 55",
    "+ 2 * 2 - 2 1",
    "+ + 10 20 30",
    "- - 1 2",
    "/ + 3 10 * + 2 3 - 3 5"
]

for input_str in input_strings:
    try:
        result = to_infix(input_str)
        print(f"Исходное выражение: {input_str}")
        print(f"Инфиксная нотация: {result}\n")
    except ValueError as e:
        print(f"Исходное выражение: {input_str}")
        print(f"Ошибка: {e}\n")