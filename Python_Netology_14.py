# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def main ():


    commands = {
    'a' : add_command,
    'l' : list_command,
    'p' : person_command,
    's' : shelf_command
    }

    check_flag = True

    while check_flag:
#        commands.get(input_code ()) () # два варианта  одинаковы
        commands[input_code()]()
        confirm = input ('Для продолжения нажмите Y\n>>')
        check_flag = False if confirm != 'Y' else True



def input_code ():
    '''
    command input
    returns a command code
    '''

    command = ' '
    check_list = ['a','l', 'p', 's']
    while command not in check_list:
        print ('Введите команду')
        command = input ('>> ')
    return command

def add_command ():
    '''
    adds a specified document to the database
    asks for
    type - str
    number - str
    name - str
    shelf - str
    '''

    type = input ('Введите тип документа\n>> ')
    number = input ('Введите номер документа\n>> ')
    name = input ('Введите имя \n>> ')
    shelf = (input ('На какую полку положить документ?\n>>'))

    documents.append ({"type": type, "number": number, "name": name})
    if shelf not in directories:
        directories[shelf] = []
    directories[shelf].append (number)

def list_command ():
    '''
    lists all existing documnents
    '''

    for document in documents:
        print ('{0}, "{1}", "{2}"'.format (document['type'], document['number'], document['name']))

def person_command ():
    '''
    prints person's name if such exist
    asks for
    number - str
    '''

    number = input ('Введите номер документа\n>> ')
    check_flag = False
    for document in documents:
        if number in document.values():
            print (document['name'])
            check_flag = True
    if check_flag == False:
        print ('Неверный номер документа')

def shelf_command ():
    '''
    prints the shelf where the document is kept
    asks for
    number - str
    '''
    number = input ('Введите номер документа\n>> ')
    check_flag = False
    for shelf in directories.keys():
        if number in directories[shelf]:
            print ('Документ лежит на полке номер %s' %(shelf))
            check_flag = True
    if check_flag == False:
        print ('Неверный номер документа')