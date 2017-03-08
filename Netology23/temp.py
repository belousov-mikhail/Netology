# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 22:51:39 2017

@author: Mikhail Belousov
"""

import yaml
import json
import pprint

with open ('recipes.yaml', 'r', encoding='utf8') as recipes_yaml:
    cook_book = yaml.load (recipes_yaml)
pprint.pprint (cook_book)


import json
with open ('recipes.json', 'r', encoding='utf8') as jsonstring:
    jsonstring = json.load(jsonstring)
pprint.pprint (jsonstring)
