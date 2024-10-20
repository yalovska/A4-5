import re


# Функція для обробки рядків і заміни поля "рік" на "YYYY"
def process_line(line):
    # Замінити всі роздільники на ;
    line = re.sub(r'[;:?]', ';', line)

    # Замінити рік на "YYYY"
    line = re.sub(r'\b(200[1-9]|20[1-9]\d)\b', 'YYYY', line)

    return line


# Функція для обробки файлу
def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            processed_line = process_line(line)
            outfile.write(processed_line + '\n')


# Використання функції для файлів
input_file = 'input.txt'  # Вхідний файл
output_file = 'output.txt'  # Вихідний файл
process_file(input_file, output_file)

print(f"Файл {output_file} успішно створено.")
