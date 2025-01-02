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
    Считывание рецепта из списка строк.
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
def create_cook_book(file_path):
    """
    Создание словаря cook_book из файла.
    """
    cook_book = {}
    lines = read_file(file_path)
    i = 0
    
    while i < len(lines):
        # Пропускаем пустые строки
        if lines[i].strip() == '':
            i += 1
            continue
        # Определяем количество строк в рецепте
        recipe_name = lines[i].strip()
        ingr_count = int(lines[i + 1].strip())
        end = i + 2 + ingr_count
        
        # Парсим рецепт и добавляем в cook_book
        recipe_name, ingredients = chg_in_dict(lines[i:end])
        cook_book[recipe_name] = ingredients
         # Переходим к следующему рецепту
        i = end
    
    return cook_book
ok_res = create_cook_book("recipes.txt")
print (ok_res)