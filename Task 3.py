def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return len(file.readlines())
a = count_lines("1.txt")
print (a)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
b = read_file("2.txt")
print(b)
def write_output(sorted_files):
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for file_path, line_count in sorted_files:
            output_file.write(f"{file_path}\n{line_count}\n{read_file(file_path)}\n\n")

def main():
    files = ['1.txt', '2.txt', '3.txt']
    # Считаем количество строк в каждом файле
    file_line_counts = [(file, count_lines(file)) for file in files]
    # Сортируем файлы по количеству строк
    sorted_files = sorted(file_line_counts, key=lambda x: x[1])
    # Записываем результат в итоговый файл
    write_output(sorted_files)

