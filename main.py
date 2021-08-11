from pprint import pprint

with open("data.txt", 'r', encoding='UTF-8') as file:
    count = 1
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
    pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    all_ingridients = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] = int(new_shop_list_item['quantity']) * person_count
            if new_shop_list_item['ingredient_name'] not in all_ingridients:
                all_ingridients[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                all_ingridients[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    pprint(all_ingridients)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
get_shop_list_by_dishes(['Омлет'], 2)
get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)
