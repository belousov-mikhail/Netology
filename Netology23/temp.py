# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 22:51:39 2017

@author: Mikhail Belousov
"""

import yaml
import json
import csv
import pprint
#
#with open ('recipes.yaml', 'r', encoding='utf8') as recipes:
#    cook_book = yaml.load (recipes)
#pprint.pprint (cook_book)
#
#
#import json
#with open ('recipes.json', 'r', encoding='utf8') as recipes
#    cook_book = json.load(recipes)
#pprint.pprint (jsonstring)



#with open ('recipes2.csv', 'r', encoding='utf8') as recipes:
#    cook_book = csv.reader(recipes, delimiter=',')
#    for row in cook_book:
#        print (row)
#        print ('ingredient_name' in row)



# сохранение в yaml с unicode
#import yaml
#cook_book = {
#    "яичница":[
#            {"ingredient_name" : "яйца", "quantity" : 2, "measure" : "шт."},
#            {"ingredient_name" : "помидоры", "quantity" : 100, "measure" : "г"},
#              ],
#    "стейк":[
#            {"ingredient_name" : "говядина", "quantity" : 300, "measure" : "г"},
#            {"ingredient_name" : "специи", "quantity" : 5, "measure" : "г"},
#            {"ingredient_name" : "масло", "quantity" : 10, "measure" : "мл"}
#              ],
#                }
#with open ('recipes_example.yaml', 'w') as recipes:
#    yaml.dump (cook_book, recipes, allow_unicode=True)

#with codecs.open(file_name, "r",encoding='utf-8', errors='ignore') as fdata:


