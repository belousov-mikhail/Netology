# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 03:34:58 2017

@author: Mikhail Belousov
"""
import chardet

def check_encoding(fname):
    rawdata = open(fname, "rb").read()
    open(fname).close()
    result = chardet.detect(rawdata)
    return result['encoding']

fname = 'newsafr.json'