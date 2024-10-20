import re

pattern = r"""
    ^\s*(?P<year>200[1-9]|20[1-9]\d)\s*                     # Рік від 2001 і далі
    [;:?]\s*(?P<patronymic>[\u0400-\u04FFa-zA-Z'’-]{1,28})\s*  # По-батькові (латиниця + кирилиця)
    [;:?]\s*(?P<name>[\u0400-\u04FFa-zA-Z'’-]{1,27})\s*        # Ім'я (латиниця + кирилиця)
    [;:?]\s*(?P<surname>[\u0400-\u04FFa-zA-Z'’-]{1,22})\s*     # Прізвище (латиниця + кирилиця)
    [;:?]\s*(?P<task>[\w .${}_]{1,59})\s*                    # Умова задачі (латиниця + спецсимволи)
    [;:?]\s*(?P<score>(100|[1-9]?[0-9]))\s*$                 # Відсоток (0-100)
"""

# Компілюємо регулярний вираз
regex = re.compile(pattern, re.VERBOSE | re.UNICODE)

# Функція для перевірки рядка
def check_line(file_line):
    match = regex.match(file_line)
    if match:
        return True
    return False

# Перевірка прикладу
line = "2005; Іванович; Олександр; Петров; Виконати задачу на суму; 85"
if check_line(line):
    print("Рядок коректний")
else:
    print("Рядок некоректний")
