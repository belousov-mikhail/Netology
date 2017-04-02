# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:11:09 2017

@author: Mikhail Belousov
"""
import requests
import os
import chardet

class TranslateIt(object):
    """
    methods
    translateit (source, **kwargs)
    translateit - translates source into output
    source - txt file to be translated
    froml - source language, if not specified, yandex tries to autodetect
    tol - translation language, default is ru
    output - translayed txt file

    attributes
    params - parameters dict for yandex api
    encoding - encoding of source file detected by _check_encoding method
    source_name, output_name - absolute paths of source and output files respectively
    code - result of translation
    message - error message if translation failed
    translated_text = translated text if succeeded

    constants
    MAX_SIZE - maximum size of a source file according to yandex api
    """

    key = 'trnsl.1.1.20170331T021116Z.53a353fef9d94e08.9617ecfdaf7fbe170972c4107aac8780e53dd21f'
    api_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    MAX_SIZE = 10000
    yandex_string = "\nTranslated by Yandex.Translate service, 'http://translate.yandex.ru/'" #added to translation result according to licence requirements


    def _get_encoding(self, file_name):
        result = chardet.detect(open(file_name, "rb").read())
        open(file_name).close()
        return result['encoding']


    def _get_source(self, source):
        if os.path.exists(source) and source.endswith('.txt'):
            #check the encoding of a source file
            self.encoding = TranslateIt._get_encoding(self, source)
            self.source_name = os.path.abspath (source)
            # if source exists, assign it's content to text parameter
            with open(self.source_name, 'r', encoding=self.encoding) as f:
                text = f.read()
            if len(text) < TranslateIt.MAX_SIZE:
                return text
            else:
                raise ValueError('File size can not be more than {} symbols'.format(TranslateIt.MAX_SIZE))
        else:
            raise FileNotFoundError('No data source file found')


    def _set_langs(froml, tol):
        if froml=='auto':
            return tol, 1
        else:
            return(froml + '-' + tol), None


    def _set_output(self, output):
        if output=='same':
            self.output_name = os.path.abspath('translated_' + self.params['lang'] + '_' + os.path.split(self.source_name)[-1])
        else:
            self.output_name = os.path.abspath(output) if output.endswith('.txt') else os.path.abspath(output +'.txt')

    def _save_output(output_name, text):
        with open(output_name, 'w', encoding='utf8') as f:
                    f.write(text)


    def translate_it(self, source, output='same', froml='auto', tol='ru'):
        self.params = {'key': TranslateIt.key}
        # get source  file
        self.params['text'] = TranslateIt._get_source(self, source)
        #create translation pair
        self.params['lang'], self.params['options'] = TranslateIt._set_langs(froml, tol)
        #create output file
        TranslateIt._set_output(self, output)
        #translate, save result in output file if succeeded
        try:
            response_result = requests.get(TranslateIt.api_url, params=self.params).json()
            self.code = response_result['code']
            if self.code != 200:
                self.message = response_result['message']
                print('Translation failed\n Error code: {0}, error message: {1}'.format(self.code, self.message))
            else:
                self.translated_text = response_result['text'][0] + TranslateIt.yandex_string
                TranslateIt._save_output(self.output_name, self.translated_text)
                print('Translation successful, result saved in {0}'.format(self.output_name))
        except Exception:
            print("Got unexpected error")
            pass





