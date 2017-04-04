# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:24:27 2017

@author: Mikhail Belousov
"""
import osa
#%%
url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
client = osa.client.Client(url)
response = client.service.ConvertTemp(Temperature=12.5, FromUnit="degreeCelsius", ToUnit = "degreeFahrenheit")
print(response)

#%%
url2 = 'http://www.webservicex.net/ConvertSpeed.asmx?WSDL'
client2 = osa.client.Client(url2)
response2 = client2.service.ConvertSpeed(speed=500, FromUnit="centimetersPersecond", ToUnit = "milesPerhour")
print(response2)

#%%

url3 = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
client3 = osa.client.Client(url3)
#print (client3.types)
#response3 = client3.service.CountryToCurrency(country='Germany', activeOnly=False)
response3 = client3.service.ConvertToNum(fromCurrency='USD', toCurrency='RUB', amount=1, rounding=True)
print (response3)