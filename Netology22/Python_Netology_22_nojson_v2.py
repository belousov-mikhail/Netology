# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 02:06:13 2017

@author: Mikhail Belousov
"""
import chardet
import os


def get_six_letter_word(json_string_entry):
    russian_letters = ''.join([chr(n) for n in range(1040, 1104)]) + 'Ёё'
    symbols_to_strip = "0123456789 !@#$%^&*()-_+={}[]|\:;'<>?,./\""
    striped_entry = json_string_entry.strip(symbols_to_strip)
    word = ''
    result_words = []
    for index, char in enumerate(striped_entry):
        if char not in russian_letters:
            if len(word) > 6:
                result_words.append(word)
            word = ''
        else:
            word += char
            if index == (len(striped_entry) - 1) and len(word) > 6:
                result_words.append(word)
    return result_words


def count_top_ten(word_dict):
    top_ten = sorted(word_dict.items(), key=lambda x: x[1],
                      reverse=True)
    return top_ten[0:10]


def get_new_entry(name, charset):
    with open(name, 'r', encoding=charset) as json_source:
        json_string = json_source.read()
    return json_string


def parser(parsing_string):
    word_dict = {}
    for entry in parsing_string.split():
        words = get_six_letter_word(entry)
        if words:
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


def print_results(news_entry, top_ten):
    print('Список из 10 самых часто встречающихся слов в файле "{}"\n'.
          format(news_entry))
    for index, word in enumerate(top_ten):
        print('{0:2}.Слово "{1}", встречается {2} раз\n'.
               format(index+1, word[0], word[1]))


def check_encoding(news_file):
    rawdata = open(news_file, "rb").read()
    result = chardet.detect(rawdata)
    open(news_file).close()
    return result['encoding']


def main():
    home_dir = os.getcwd()  # put files in home dir by default
    news_files = []
    for file in os.listdir(home_dir):
        whole_file_name = os.path.join(home_dir, file)
        if file.endswith('.json'):
            news_files.append(whole_file_name)

    for news_entry in news_files:
        charset = check_encoding(news_entry)
        parsing_string = get_new_entry(news_entry, charset)
        word_dict = parser(parsing_string)
        top_ten = count_top_ten (word_dict)
        print_results(news_entry, top_ten)

main()
