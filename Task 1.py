# Задание 1
def read_file(file_path):
    """
    Чтение файла построчно с использованием цикла.
    """
    list_of_lines = []
    with open(file_path, "r") as f:
        for line in f:
            list_of_lines.append(line.strip())
    return list_of_lines
