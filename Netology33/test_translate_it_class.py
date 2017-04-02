# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:49:35 2017

@author: Mikhail Belousov
"""
from translate_it_class import TranslateIt as T

# uses files in Examples folder to test TraslateIt class
a = T()
test_dir = './Examples'
os.chdir (test_dir)
for file in os.listdir(os.getcwd()):
    if file.endswith('.txt'):
        a.translateIt(file)


