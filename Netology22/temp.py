# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:08:57 2017

@author: Mikhail Belousov
"""


# import json
# сделать версию через json.loads pprint

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


def print_results(news_entry, frequent_words):
    print('Список из 10 самых часто встречающихся слов в файле "{}"'.format(news_entry))
    for counts, word in frequent_words.items():
        print('{0:2}: {1:13}, встречается {2:2} раз'.format(counts, word[1], word[0]))


def main():
    encoding_dict = {'newsafr.json': 'utf8',
                     'newscy.json': 'koi8_r',
                     'newsfr.json': 'iso8859_5',
                     'newsit.json': 'cp1251'}
    for news_entry, charset in encoding_dict.items():
        parsing_string = get_new_entry(news_entry, charset)
        word_dict = parser(parsing_string)
        frequent_words = count_frequent(word_dict)
        print_results(news_entry, frequent_words)


main()
