# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:34:57 2017

@author: Mikhail Belousov
"""
"""в этой версии
- чтение рецептов из json\yaml
- функция добавления нового рецепта, чтобы протестировать запись
- запись словаря с новым рецептом сразу в файлы всех форматов
(сейчас json\yaml)
"""
import yaml
import json
import codecs


def get_recipes(data_type):
    modules = {'yaml': yaml,
                  'json': json}
    cook_book = {}
    file_name = 'recipes.'+data_type
    with open(file_name, 'r', encoding='utf') as recipes:
        cook_book = modules[data_type].load(recipes)
    return cook_book


def add_new_recipe(cook_book, data_type):
    dish_name = input("Введите название блюда\n>>").lower()
    cook_book_entry = {}
    cook_book_entry[dish_name] = []
    while True:
        ingredient_name = input("Введите название ингредиента или С для завершения:\n>>")
        if ingredient_name == "С":
            break
        measure = input("Введите единицу измерения:\n>>")
        quantity = float(input("Введите количество:\n>>"))
        cook_book_entry[dish_name].append({'ingredient_name': ingredient_name,
                       'measure': measure, 'quantity': quantity})
        cook_book.update(cook_book_entry)
    with codecs.open('recipes.yaml', 'w', encoding='utf-8', errors='ignore') as recipes:
        yaml.dump(cook_book, recipes, allow_unicode=True)

    with codecs.open('recipes.json', 'w', encoding='utf-8', errors='ignore') as recipes:
        json.dump(cook_book, recipes, ensure_ascii=False)
    return get_recipes (data_type)


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item["quantity"] *= person_count
            if new_shop_list_item["ingredient_name"] not in shop_list:
                shop_list[new_shop_list_item["ingredient_name"]] = new_shop_list_item
            else:
                shop_list[new_shop_list_item["ingredient_name"]]["quantity"] += new_shop_list_item["quantity"]
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print("{ingredient_name} {quantity} {measure}".format(**shop_list_item))


def create_shop_list(cook_book):
    print ("Доступные блюда:", ' \n'.join([dish for dish in cook_book.keys()]))
    person_count = int(input("Введите количество человек >>"))
    input_flag = False
    while not input_flag:
        dishes = input("Введите блюда в расчете на одного человека (через запятую)\n>>").lower().split(', ')
        for dish in dishes:
            input_flag = dish in cook_book.keys()
            if not input_flag:
                print("Неверный ввод, повторите")
                break
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)
    return

def main ():
    print ("Учебная программа для изучения форматов данных.\n")
    while True:
        print ("1 - добавить блюдо,\n2 - распечатать список покупок")
        chosen_action = input('>>')
        data_type = input ("Выберите тип файла (yaml\json)\n>>").lower()
        if chosen_action == '1':
            cook_book = add_new_recipe (get_recipes(data_type), data_type)
        else:
            create_shop_list(get_recipes(data_type))
        user_input = input ('Для продолжения нажмите Д\n>>')
        if user_input != 'Д':
            break

main ()