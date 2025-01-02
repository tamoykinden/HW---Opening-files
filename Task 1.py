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
rec = read_file("recipes.txt")
print (rec)
def chg_in_dict (lines):
    """
    Парсинг рецепта из списка строк.
    """
    recipe_name = lines[0].strip()
    ing_count = int(lines[1].strip())
    ingr = []
    for line in lines[2:2 + ing_count]:
        ingredient_name, quantity, measure = line.strip().split(' | ')
        ingr.append({
            'ingredient_name': ingredient_name,
            'quantity': int(quantity),
            'measure': measure
        })
    return recipe_name, ingr 
res = chg_in_dict(rec)
print(res)