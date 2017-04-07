# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:22:55 2017

@author: Mikhail Belousov
"""

import glob
import os.path
import chardet


def get_encoding(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            encoding = chardet.detect(f.read())['encoding']
        return encoding
    else:
        raise FileNotFoundError ('File not found')

def search_key(files, check_smb):
    result_files = []
    for file in files:
        encoding = get_encoding(file)
        for line in open(file, 'r', encoding=encoding):
            if check_smb in line:
                result_files.append(file)
                break
    return result_files


def main():
    home_dir = os.getcwd()
    source_dir = 'Advanced Migrations'
    file_list = glob.glob(os.path.join(home_dir, source_dir, "*.sql"))
    while True:
        check_smb = input("Введите строку\n>>")
        new_file_list = search_key(file_list, check_smb)
        for file in new_file_list:
            print(os.path.split(file)[-1])
        print('Всего найдено файлов: {}'.format(len(new_file_list)))
        file_list = new_file_list

#def main():
#    home_dir = os.getcwd()
#    source_dir = 'Migrations'
#    file_list = glob.glob(os.path.join(home_dir, source_dir, "*.sql"))
#    while True:
#        check_smb = input("Введите строку\n>>")
#        new_file_list = search_key(file_list, check_smb)
#        for file in new_file_list:
#            print(os.path.split(file)[-1])
#        print('Всего найдено файлов: {}'.format(len(new_file_list)))
#        stop_flag = input("Для завершения нажмите с или С\n>>")
#        if stop_flag == 'с' or stop_flag == 'С':
#            print('Конец сеанса')
#            break
#        else:
#            file_list = new_file_list
#            continue


if __name__ == '__main__':
    main()


