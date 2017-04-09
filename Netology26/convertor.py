# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 13:21:25 2017

@author: Mikhail Belousov
"""
import subprocess
import os

source_dir = os.path.join(os.getcwd(), 'Source')
if not os.path.exists('Output'):
    os.mkdir('Output')
output_dir = os.path.join(os.getcwd(), 'Output')

for file in os.listdir(source_dir):
    if file.endswith('.jpg'):
        source_file = os.path.join(source_dir, file)
        result_file = os.path.join(output_dir, file)
        command = 'convert.exe '+ source_file + ' -resize 200 ' + result_file
        subprocess.run(command)




