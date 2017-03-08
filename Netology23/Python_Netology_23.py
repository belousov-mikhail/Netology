# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:34:57 2017

@author: Mikhail Belousov
"""

import yaml
import json

# cook_book = {
#    "яичница":[
#            {"ingredient_name" : "яйца", "quantity" : 2, "measure" : "шт."},
#            {"ingredient_name" : "помидоры", "quantity" : 100, "measure" : "г"},
#              ],
#    "стейк":[
#            {"ingredient_name" : "говядина", "quantity" : 300, "measure" : "г"},
#            {"ingredient_name" : "специи", "quantity" : 5, "measure" : "г"},
#            {"ingredient_name" : "масло", "quantity" : 10, "measure" : "мл"}
#              ],
#    "салат":[
#            {"ingredient_name" : "помидоры", "quantity" : 100, "measure" : "г"},
#            {"ingredient_name" : "огурцы", "quantity" : 100, "measure" : "г"},
#            {"ingredient_name" : "масло", "quantity" : 100, "measure" : "мл"},
#            {"ingredient_name" : "лук", "quantity" : 1, "measure" : "шт."}
#                ]
#                }
# cook_book = {}


def get_yaml(file_name):
    with open(file_name, 'r', encoding='utf8') as recipes_yaml:
        cook_book = yaml.load(recipes_yaml)
    return cook_book


def get_json(file_name):
    with open(file_name, 'r', encoding='utf8') as recipes_json:
        cook_book = json.load(recipes_json)
    return cook_book


def get_csv(file_name):
    pass

def get_recipes(chosen_format):
    formats_dict = {'yaml': lambda: get_yaml(file_name),
                  'json': lambda: get_json(file_name),
                  'csv': lambda: get_csv(file_name)}
    cook_book ={}
    file_name = 'recipes.'+chosen_format
    cook_book = formats_dict[chosen_format]()
    return cook_book


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

def main ():
    print ("Учебная программа для изучения форматов данных.\n")
    chosen_format = input ("Выберите тип файла (yaml\json\csv)\n>>").lower()
    create_shop_list (get_recipes (chosen_format))

main ()