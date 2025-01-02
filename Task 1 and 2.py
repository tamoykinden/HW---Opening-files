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
#print (rec)
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
# print(res)
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
        
        # Считываем рецепт и добавляем в cook_book
        recipe_name, ingredients = chg_in_dict(lines[i:end])
        cook_book[recipe_name] = ingredients
         # Переходим к следующему рецепту
        i = end
    
    return cook_book
ok_res = create_cook_book("recipes.txt")
# print (ok_res)

#Задание 2
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
    Формирует список ингредиентов для приготовления указанных блюд на заданное количество персон.
    """
    shop_list = {}  # Словарь для хранения итогового списка ингредиентов

    # Проходим по каждому блюду
    for dish in dishes:
        # Проверяем, есть ли блюдо в cook_book
        if dish in cook_book:
            # Проходим по каждому ингредиенту блюда
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count  # Учитываем количество персон

                # Если ингредиент уже есть в списке, суммируем количество
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' отсутствует в cook_book.")

    return shop_list
res1 = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, ok_res)
print(res1)