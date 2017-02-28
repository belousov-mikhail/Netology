# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:34:57 2017

@author: Mikhail Belousov
"""

# яичница  яйца 2 шт, помидор 100 г
# стейк 300 г мяса, 5 г специи, 10 мл масло
# салат помидоры 100 г, огурцы 100 г, масло 100 мл, лук 1 шт

#dishes = ["яичница", "стейк", "стейк"]


cook_book = {
	"яичница":[
	        {"ingredient_name" : "яйца", "quantity" : 2, "measure" : "шт."},
	        {"ingredient_name" : "помидоры", "quantity" : 100, "measure" : "г"},
	          ],
	"стейк":[
	        {"ingredient_name" : "говядина", "quantity" : 300, "measure" : "г"},
	        {"ingredient_name" : "специи", "quantity" : 5, "measure" : "г"},
	        {"ingredient_name" : "масло", "quantity" : 10, "measure" : "мл"}
	          ],
	"салат":[
	        {"ingredient_name" : "помидоры", "quantity" : 100, "measure" : "г"},
	        {"ingredient_name" : "огурцы", "quantity" : 100, "measure" : "г"},
	        {"ingredient_name" : "масло", "quantity" : 100, "measure" : "мл"},
	        {"ingredient_name" : "лук", "quantity" : 1, "measure" : "шт."}
		        ]
		        }

def get_shop_list_by_dishes (dishes, person_count):
  shop_list = {}

  for dish in dishes:
    for ingredient in cook_book[dish]:
      new_shop_list_item = dict (ingredient)
      new_shop_list_item["quantity"] *= person_count
      if new_shop_list_item["ingredient_name"] not in shop_list:
        shop_list[new_shop_list_item["ingredient_name"]] = new_shop_list_item
      else:
        shop_list[new_shop_list_item["ingredient_name"]]["quantity"] += new_shop_list_item ["quantity"]
  return shop_list

def print_shop_list (shop_list):
  for shop_list_item in shop_list.values():
    print ("{ingredient_name} {quantity} {measure}".format (**shop_list_item))

def create_shop_list ():
  person_count = int (input ("Введите количество человек >>"))
  dishes = input ("Введите блюда в расчете на одного человека (через запятую) >>").lower().split (', ')
  shop_list = get_shop_list_by_dishes (dishes, person_count)
  print_shop_list (shop_list)

create_shop_list ()
