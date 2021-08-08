from pprint import pprint

with open("data.txt", 'r', encoding='UTF-8') as file:
    count = 0
    for line in file:
        if line == '\n':
            count += 1
with open("data.txt", 'r', encoding='UTF-8') as file:
    cook_book = {}
    for i in range(count):
        dish = file.readline().strip()
        ingridients = []
        ingridients_amount = int(file.readline())
        for i in range(ingridients_amount):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            ingridients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = ingridients
        file.readline()
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    all_ingridients = {}
    for dish in dishes:
        if dish in cook_book:
            ingridients = cook_book[dish]
            for ingridient in ingridients:
                quantity = int(ingridient['quantity']) * person_count
                measure = ingridient['measure']
                ingredient_name = ingridient['ingredient_name']
                dict = {'measure': measure, 'quantity': quantity}
                all_ingridients[ingredient_name] = dict
    pprint(all_ingridients)


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)
