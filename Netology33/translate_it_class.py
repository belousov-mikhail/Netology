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
    encoding - encoding of source file detected by _checkEncoding method
    source_name, output_name - absolute paths of source and output files respectively
    code - result of translation
    message - error message if translation failed
    translated = translated text if succeeded

    constants
    MAX_SIZE - maximum size of a source file according to yandex api
    """

    key = 'trnsl.1.1.20170331T021116Z.53a353fef9d94e08.9617ecfdaf7fbe170972c4107aac8780e53dd21f'
    api_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    MAX_SIZE = 10000
    yandex_string = "\nTranslated by Yandex.Translate service, 'http://translate.yandex.ru/'" #added to translation result according to licence requirements

    #check the encoding of a source file
    def _checkEncoding(self, file_name):
        result = chardet.detect(open(file_name, "rb").read())
        open(file_name).close()
        return result['encoding']


    #translates source to output
    def translateIt(self, source, **kwargs):
        self.params = {'key': TranslateIt.key}
        #check if kwargs are valid
        kwargs_tuple = ('output', 'froml', 'tol')
        if not all([key in kwargs_tuple for key in kwargs.keys()]):
            raise NameError ('Invalid named parameter')
        # check if source file exists
        if os.path.exists(source) and source.endswith('.txt'):
            self.encoding = TranslateIt._checkEncoding(self, source)
            self.source_name = os.path.abspath (source)
            # if source exists, assign it's content to text parameter
            with open(self.source_name, 'r', encoding=self.encoding) as f:
                text = f.read()
                if len (text) < TranslateIt.MAX_SIZE:
                    self.params['text'] = text
                else:
                    raise ValueError('File size can not be more than {} symbols'.format(TranslateIt.MAX_SIZE))
        else:
            raise FileNotFoundError('No data source file found')

        #create translation pair
        if 'tol' not in kwargs.keys():
            kwargs['tol'] = 'ru'
        if 'from' not in kwargs.keys():
            self.params['options'] = 1
            self.params['lang'] = kwargs['tol']
        else:
            self.params['lang'] = kwargs['froml'] + '-' + kwargs['tol']

        #create output file:
        if 'output' in kwargs.keys():
            self.output_name = os.path.abspath(kwargs['output']) if kwargs['output'].endswith('.txt') else os.path.abspath(kwargs['output'] +'.txt')
        else:
            self.output_name = os.path.abspath('translated_' + self.params['lang'] + '_' + os.path.split(self.source_name)[-1])


        #translate, save result in output file if succeeded
        response_result = requests.get(TranslateIt.api_url, params=self.params).json()
        self.code = response_result['code']
        if self.code != 200:
            self.message = response_result['message']
            print ('Translation failed\n Error code: {0}, error message: {1}'.format(self.code, self.message))
        else:
            self.translated = response_result['text'][0] + TranslateIt.yandex_string
            with open(self.output_name, 'w', encoding='utf8') as f:
                f.write(self.translated)
            print ('Translation successful, result saved in {0}'.format(self.output_name))


