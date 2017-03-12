# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:34:57 2017

@author: Mikhail Belousov
"""
import json
import yaml
import csv
import ast


#this block builds cook_book from recipes.txt
def store_recipe(recipe):
    cook_book_entry = {}
    dish_name = recipe[0].lower().strip()
    cook_book_entry[dish_name] = []
    ingredients_quantity = int(recipe[1])
    for index in range(ingredients_quantity):
        ingredient = recipe[index+2].split('|')
        cook_book_entry[dish_name].append({"ingredient_name": ingredient[0].lower().strip(), "quantity": int(ingredient[1]), "measure": ingredient[2].lower().strip()})
    return cook_book_entry


def get_provided_recipes():
    cook_book = {}
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


#this block creates\updates initial files in suppurted formats from cook_book
def do_formatted_files(cook_book):
# create json file
    with open('recipes.json', 'w', encoding='utf8', errors='ignore') as recipes_json:
        json.dump(cook_book, recipes_json, ensure_ascii=False, indent=2)
# create yaml file
    with open('recipes.yaml', 'w', encoding='utf8', errors='ignore') as recipes_yaml:
        yaml.dump(cook_book, recipes_yaml, allow_unicode=True, indent=2)
# create csv file
    with open('recipes.csv', 'w', encoding='utf8', errors='ignore', newline='') as recipes_csv:
        recipewriter = csv.writer(recipes_csv)
        for dish_name, ingredients in cook_book.items():
            recipewriter.writerow([dish_name])
            recipewriter.writerows((ingredients,))


#this block contains reading function for all datatypes:
def get_recipes(datatype):
    cook_book = {}
    file_name = 'recipes.' + datatype
    if datatype == 'csv':
        with open (file_name, 'r', encoding='utf8', errors='ignore', newline='') as recipes:
            recipereader = csv.reader(recipes)
            for row in recipereader:
                if len(row) == 1 :
                    dish = str(row).strip("'[]")
                    cook_book[dish] = []
                    for entry in next(recipereader):
                        cook_book[dish].append(ast.literal_eval(entry))
        return cook_book

    if datatype == 'json':
        with open(file_name, 'r', encoding='utf', errors='ignore') as recipes:
            cook_book = json.load(recipes)
        return cook_book

    if datatype == 'yaml':
        with open(file_name, 'r', encoding='utf', errors='ignore') as recipes:
            cook_book = yaml.load(recipes)
        return cook_book



