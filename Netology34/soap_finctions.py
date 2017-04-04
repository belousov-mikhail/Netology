# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 12:06:32 2017

@author: Mikhail Belousov
"""

#%%
import chardet
import os
import osa

def get_source(file):
    if os.path.exists(file):
        encoding = chardet.detect(open(file, "rb").read())['encoding']
        open(file).close()

        data = []
        with open(file, "r", encoding=encoding) as f:
            for line in f.readlines():
                data.append(line.strip())
        return data
    else:
        raise FileNotFoundError('No such file found')

def fahr_to_cel(file):
    data = get_source(file)
    url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.client.Client(url)
    total_fahr = 0
    for el in data:
        total_fahr += float(el[:2])
    average_fahr = total_fahr/len(data)
    response = client.service.ConvertTemp(Temperature=average_fahr, FromUnit="degreeFahrenheit", ToUnit = "degreeCelsius")
    print("This week's average temperature in Celsius is {0:0.2f}".format(response))


def convert_to_one_currency(file):
    data = get_source(file)
    url = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client = osa.client.Client(url)
    total_spendings = 0
    needed_currency = 'RUB'
    for el in data:
        _, price, converted_currency = el.split()
        response = client.service.ConvertToNum(fromCurrency=converted_currency, toCurrency=needed_currency, amount=price, rounding=True)
        total_spendings += response
    print("Total spendings are {0} RUB".format(round(total_spendings, 0)))


def calculate_whole_distance(file):
    data = get_source(file)
    url = 'http://www.webservicex.net/length.asmx?WSDL'
    client = osa.client.Client(url)
    total_distance = 0
    units = {'mi': 'Miles'} # возможного расширения
    needed_unit = 'Kilometers'
    for el in data:
        print (el)
        _, distance, converted_unit = el.split()
        if ',' in distance:
            distance = float(''.join([char for char in distance if char != ',']))
        else:
            distance = float(distance)
        response = client.service.ChangeLengthUnit(LengthValue=distance, fromLengthUnit=units[converted_unit], toLengthUnit=needed_unit)
        print(response)
        total_distance += response
    print("Total distance is {0} kms".format(round(total_distance, 2)))


