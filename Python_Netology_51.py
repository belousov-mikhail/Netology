# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 01:28:35 2017

@author: Mikhail Belousov
"""

#file creation date = test passing date

mass = [x for x in range(1, 101)]

list = [x**3 for x in mass if x % 3 == 0 and x % 4 == 0]