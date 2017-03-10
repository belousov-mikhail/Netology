# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 02:06:13 2017

@author: Mikhail Belousov
"""
import chardet
import os
import json


def check_encoding(news_file):
    rawdata = open(news_file, "rb").read()
    result = chardet.detect(rawdata)
    open(news_file).close()
    return result['encoding']


def get_new_entry(name, charset):
    with open(name, 'r', encoding=charset) as json_source:
        json_dict = json.load(json_source)
    return json_dict


def decoding_json(from_json_data, data_type, storage):
    if data_type == dict:
        for value in from_json_data.values():
            decoding_json(value, type(value), storage)
    elif data_type == list:
        for value in from_json_data:
            decoding_json(value, type (value), storage)
    else:
        storage.append(from_json_data)
    return storage


def get_word_dict(parsed_json_list):
    word_dict = {}
    for entry in parsed_json_list:
        words = get_six_letter_word(str(entry))
        if words:
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


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
              reverse=True)[0:10]
    return top_ten


def print_results(news_entry, top_ten):
    print('Список из 10 самых часто встречающихся слов в файле "{}"\n'.
          format(news_entry))
    for index, word in enumerate(top_ten):
        print('{0:2}.Слово "{1}", встречается {2} раз\n'.
               format(index + 1, word[0], word[1]))


def main():
    home_dir = os.getcwd()  # put files in home dir by default
    news_files = []
    for file in os.listdir(home_dir):
        whole_file_name = os.path.join(home_dir, file)
        if file.endswith('.json'):
            news_files.append(whole_file_name)
    for news_entry in news_files:
        charset = check_encoding(news_entry)
        dict_to_parse = get_new_entry(news_entry, charset)
        parsed_json_list  = decoding_json(dict_to_parse, type(dict_to_parse), [])
        word_dict = get_word_dict(parsed_json_list)
        top_ten = count_top_ten(word_dict)
        print_results(news_entry, top_ten)

main()
