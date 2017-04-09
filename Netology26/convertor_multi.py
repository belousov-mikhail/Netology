# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 13:21:25 2017

@author: Mikhail Belousov
"""
import subprocess
import os
from multiprocessing import Pool

def convert(el):
    command = 'convert.exe '+ el[0] + ' -resize 200 ' + el[1]
    subprocess.run(command)

if __name__ == '__main__':

    source_dir = os.path.join(os.getcwd(), 'Source')
    if not os.path.exists('Output'):
        os.mkdir('Output')
    output_dir = os.path.join(os.getcwd(), 'Output')
    files = []

    for file in os.listdir(source_dir):
        if file.endswith('.jpg'):
            files.append((os.path.join(source_dir, file), os.path.join(output_dir, file)))

    with Pool(processes=4) as pool:
        pool.map(convert, files)




