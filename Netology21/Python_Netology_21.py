# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:30:36 2017

@author: Mikhail Belousov
"""

#Имеется список студентов, у каждого из которых есть следующие характеристики: имя, фамилия, пол, предыдущий опыт в программировании (бинарная переменная), 5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по 10-балльной шкале. Необходимо написать программу, которая в зависимости от запроса пользователя будет выводить:
#
#среднюю оценку за домашние задания и за экзамен по всем студентам;
#среднеюю оценку за домашние задания и за экзамен по студентам в разрезе: а) пола б) наличия опыта;
#определять лучшего студента/ов, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен.
#Студентов должно быть не менее 6.

students = {
            'Петренко Петр' : {'sex' : 'M', 'isSkilled' : False, 'home' : [8, 7, 10, 10, 9], 'exam' : [9]},
            'Ветренная Лиза' : {'sex' : 'F', 'isSkilled' : False, 'home' : [6, 9, 6, 4, 7], 'exam' : [7]},
            'Долбаев Алексей' : {'sex' : 'M', 'isSkilled' : True, 'home' : [9, 0, 10, 10, 8], 'exam' : [9]},
            'Неврубенко Федор' : {'sex' : 'M', 'isSkilled' : False, 'home' : [5, 6, 5, 7, 7], 'exam' : [6]},
            'Докучаев Спиридон' : {'sex' : 'M', 'isSkilled' : False, 'home' : [10, 10, 9, 8, 10], 'exam' : [7]},
            'Трахтенберг Анфиса' : {'sex' : 'F', 'isSkilled' : True, 'home' : [10, 10, 9, 10, 9], 'exam' : [10]},
            'Сельпов Иван' : {'sex' : 'M', 'isSkilled' : False, 'home' : [9, 8, 7, 8, 9], 'exam' : [10]},
            'Битюк Арсений' : {'sex' : 'M', 'isSkilled' : True, 'home' : [10, 10, 9, 10, 9], 'exam' : [10]},
        }

# константы для задания длины списков home, exam
# при необходимости можно их изменять
HOME_LENGTH = 5
EXAM_LENGTH = 1

def update_students_average (students):
    """Returns list of average grades of all students"""
    for student, value in students.items():
        home_average = sum(value['home']) / HOME_LENGTH
        exam_average = sum(value['exam']) / EXAM_LENGTH
        value['home_average'] = round(home_average, 2)
        value['exam_average'] = round(exam_average, 2)


def get_total_average():
    """Prints total average grades"""
    update_students_average(students)
    total_home = 0
    total_exam = 0
    number_students = len (students)
    print ('Средние оценки:')
    print ('{0:18} {1:14} {2:8}'.format('ФИО студента:', 'За дом. задания:', 'За экзамен:'))
    for student, value in students.items():
        print ('{0:18} {1:^14.2f} {2:^8.2f}'.format(student, value['home_average'], value['exam_average']))
        total_home += value['home_average']
        total_exam += value['exam_average']
    print ('_'*45)
    print ('{0:18} {1:^14.2f} {2:^8.2f}'.format('ИТОГО', total_home/number_students, total_exam/number_students))

def print_sorted (isTrue, key, sorted_students, average_home, average_exam):
    """Prints formatted sorting results"""
    secondline_dict = {
            'isSkilled': {True: 'С опытом разработки софта\n', False: 'Без опыта разработки софта\n'},
            'sex':{True: 'ЮНОШИ\n', False: 'ДЕВУШКИ\n'},
                      }
    print (secondline_dict[key][isTrue])
    print('{0:18} {1:14} {2:8}'.format('ФИО студента:', 'За дом. задания:', 'За экзамен:'))
    [print('{0:18} {1:^14.2f} {2:^8.2f}'.format(entry[1], entry[2], entry[3])) for entry in sorted_students if entry[0] is isTrue]
    print ('_'*45)
    print ('{0:18} {1:^14.2f} {2:^8.2f}\n'.format('ИТОГО', average_home, average_exam))

def sorted_average (key):
    """Prints list of average grades,
    sorted by key (sex\isSkilled)"""
    if key not in ['sex', 'isSkilled']:
        key = 'sex'
    sort_base = {False: False, True: True, 'M': True, 'F': False}
    update_students_average(students)
    sorted_students = []
    number_students = len (students)
    for student, value in students.items():
        entry = [sort_base[value.get(key)], student, value['home_average'], value['exam_average']]
        sorted_students.append(entry)
        sorted_students.sort()
        total_True, total_average_home_True, total_average_exam_True = 0, 0, 0
        total_False, total_average_home_False, total_average_exam_False = 0, 0, 0
    for entry in sorted_students:
        if entry[0]:
            total_True += 1
            total_average_home_True += entry[2]
            total_average_exam_True += entry[3]
        else:
            total_False += 1
            total_average_home_False += entry[2]
            total_average_exam_False += entry[3]
    headline_dict = {'sex': 'полу', 'isSkilled' : 'наличию опыта'}

    print('Средние оценки с сортировкой по {}'.format(headline_dict[key]))
# print if attribute is True
    print_sorted (True, key, sorted_students, total_average_home_True/total_True, total_average_exam_True/total_True)
#print if attribute is False
    print_sorted (False, key, sorted_students, total_average_home_False/total_False, total_average_exam_False/total_False)

def max_grade (students):
    """Prints student with a maximum grade"""
    total_grades = {}
    update_students_average (students)
    for student, value in students.items():
        total_grade = value['home_average'] * 0.6 + value['exam_average'] * 0.4
        total_grades[student] = total_grade
    max_grade = max (total_grades.values())
    print ('Максимальный бал {} у следующих студентов:'.format (max_grade))
    for student, grade in total_grades.items():
        if grade == max_grade:
            print (student)

def add_student (students): # added to make more testing
    """ Adds new entry to the dict"""
    home_length = len (students)
    student = input ('Введите имя студента в формате "Иванов Иван":\n>>')
    if student in students.keys():
        print ('Такой студент уже в базе данных')
        return
    sex = input ('Введите пол M (мужской) или F (женский):\n>>')
    isSkilled =True if input ('Есть ли опыт работы программистом (Y\\N): \n>> ') == 'Y' else False
    home = [int(input ('Оценка за задание №{}:\n>>'.format (n))) for n in range (1, HOME_LENGTH+1) ]
    exam = [int(input ('Оценка за экзамен №{}:\n>>'.format (n))) for n in range (1, EXAM_LENGTH+1) ]
    students[student] = {'sex' : sex, 'isSkilled' : isSkilled, 'home' : home, 'exam' : exam}
    print ('Студент успешно добавлен в базу')


def main():
    commands = {
    '1' : get_total_average,
    '2' : lambda: sorted_average ('sex'),
    '3' : lambda: sorted_average ('isSkilled'),
    '4' : lambda: max_grade (students),
    'a' : lambda: add_student (students)
    }
    while True:
        while True:
            print('Список команд: \n')
            print ('a - добавить данные о новом студенте\n')
            print('1 - для средней оценки за домашние задания и за экзамен по всем студентам \n')
            print('2 - среднюю оценку за домашние задания и за экзамен по студентам в разрезе пола\n')
            print('3 - среднюю оценку за домашние задания и за экзамен по студентам в разрезе опыта\n')
            print('4 - для определения лучшего студента')
            command = input ('>> ')
            command_list = ['1', '2', '3', '4', 'a']
            if command  in command_list:
                break
            print ('Неверная команда, попробуйте еще')
        commands[command] ()
        ask_further = input ('Для продолжения нажмите Y\n>>')
        if ask_further != 'Y':
            print ('До следующего раза!')
            break

main ()


