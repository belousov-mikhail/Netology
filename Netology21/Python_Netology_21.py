# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:34:57 2017

@author: Mikhail Belousov
"""
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


def store_recipe(recipe):
    cook_book_entry = {}
    dish_name = recipe[0].lower().strip()
    cook_book_entry[dish_name] = []
    ingredients_quantity = int(recipe[1])
    for index in range(2,ingredients_quantity):
        ingredient = recipe[index ].split('|')
        cook_book_entry[dish_name].append({"ingredient_name": ingredient[0].lower().strip(), "quantity": int(ingredient[1]),
                                     "measure": ingredient[2].lower().strip()})
    return cook_book_entry

def get_recipes():
    cook_book ={}
    with open('recipes.txt', 'r') as recipes:
        recipe = []
        for entry in recipes:
            entry = entry.strip()
            if entry == '':
                cook_book.update(store_recipe(recipe))
                recipe = []
            else:
                recipe.append(entry)
        cook_book.update(store_recipe(recipe))
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


def create_shop_list():
    cook_book = get_recipes()
    person_count = int(input("Введите количество человек >>"))
    dishes = input("Введите блюда в расчете на одного человека (через запятую) >>").lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)



create_shop_list()
