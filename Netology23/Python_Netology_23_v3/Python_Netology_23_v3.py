# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:34:57 2017

@author: Mikhail Belousov
"""
"""
in this bulid:
- handles json\yaml\csv
- able to add new recipes
- add and erase new recipes in json\yaml\csv
"""
import os
from helper_functions import *


def add_new_recipe(cook_book, datatype):
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
        do_formatted_files(cook_book)
    return get_recipes (datatype)


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


def program_menu():
# commands for main menu
    commands = {
            '1': lambda: add_new_recipe(get_recipes(datatype), datatype),
            '2': lambda: create_shop_list(get_recipes(datatype)),
            '3':  lambda: do_formatted_files (get_provided_recipes())}
    supported_types = ('json', 'yaml', 'csv')
# some fool-proof to escape misinputs while testing
    while True:
        print("----------")
        print("1 - добавить блюдо")
        print("2 - распечатать список покупок")
        print("3 - удалить добавленные рецепты")
        print("----------")
        chosen_action = input('>>')
        if chosen_action not in ['1', '2', '3']:
            chosen_action = '2'
        if chosen_action != '3':
            datatype = input("Введите тип файла (yaml\json\csv)\n>>").lower()
            print("----------")
            datatype = datatype if datatype in supported_types else 'yaml'
        commands[chosen_action]()
        user_input = input('Для продолжения нажмите Д\n>>')
        if user_input != 'Д':
            break


def main():
# check whether the home dir has formatted files:
    print("Учебная программа для изучения форматов данных.\n")
    home_dir = os.getcwd()
    recipe_files = ['recipes.json', 'recipes.csv', 'recipes.yaml']
    exist_flag = True
    for file in recipe_files:
        exist_flag = exist_flag and (file in os.listdir(home_dir))
# if no files, create then form provided txt
    if not exist_flag:
        print("Не обнаружены файлы изучаемых форматов.\n")
        print("Создание файлов.\n")
        cook_book = get_provided_recipes()
        do_formatted_files(cook_book)
# main menu loop
    program_menu()


if __name__ == '__main__':
    main ()