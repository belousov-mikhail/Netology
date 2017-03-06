# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 02:06:13 2017

@author: Mikhail Belousov
"""
import chardet
import os
import json


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


def count_frequent(word_dict):
    most_frequent = max(word_dict.values())
    frequent_words = {}
    counter = 0
    while counter < 10:
        for word, frequency in word_dict.items():
            if frequency == most_frequent:
                counter += 1
                frequent_words[counter] = (most_frequent, word)
        most_frequent -= 1
    return frequent_words

def get_new_entry(name, charset):
    with open(name, 'r', encoding=charset) as json_source:
        json_string = json.load(json_source)
    return json_dict


def parser(parsing_dict):
    path = parsing_dict['rss']['channel']['item']
    news_text_string = ''
    for index, entry in enumerate (path):
        news_text_string += path[index]['description']['__cdata']
        news_text_string += path[index]['title']['__cdata']
    word_dict = {}
    for entry in news_text_string.split():
        words = get_six_letter_word(entry)
        if words:
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


def print_results(news_entry, frequent_words):
    print('Список из 10 самых часто встречающихся слов в файле "{}"'.format(news_entry))
    for counts, word in frequent_words.items():
        print('{0:2}: {1:13}, встречается {2:2} раз'.format(counts, word[1], word[0]))


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
        parsing_dict = get_new_entry(news_entry, charset)
        word_dict = parser(parsing_dict)
        frequent_words = count_frequent(word_dict)
        print_results(news_entry, frequent_words)

main()
