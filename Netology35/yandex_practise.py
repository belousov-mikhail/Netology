# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 09:30:49 2017

@author: Mikhail Belousov
"""
from urllib.parse import urlencode, urlparse, urljoin
from pprint import pprint
import requests

AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
APP_ID = '57df46e1975742c19aaf8a69b26d7547'

auth_data = {'response_type': 'token',
             'client_id': APP_ID}

#print ('?'.join((AUTHORIZE_URL, urlencode(auth_data))))



class YandexMetrika (object):
    _METRIKA_STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/'
    _METRIKA_MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    token = None

    def __init__(self, token):
        self.token = token

    def get_header(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token),
                'User-Agent':'Mozilla/5.0'
        }

    @property
    def counter_list(self):
        url = urljoin(self._METRIKA_MANAGEMENT_URL, 'counters')
        headers = self.get_header()
        response = requests.get(url, headers=headers)
        counter_list=[c['id'] for c in response.json()['counters']]
        return counter_list

    def get_visits_count(self, counter_id):
        url = urljoin(self._METRIKA_STAT_URL, 'data')
        headers = self.get_header()
        params = {
                'id': counter_id,
                'metrics': 'ym:s:visits'
        }
        response = requests.get(url, params,headers=headers)
        visits_count=response.json()['data'][0]['metrics'][0]
        return visits_count

    def get_page_views(self, counter_id):
        url = urljoin(self._METRIKA_STAT_URL, 'data')
        headers = self.get_header()
        params = {
                'id': counter_id,
                'metrics': 'ym:s:pageviews'
        }
        response = requests.get(url, params,headers=headers)
        page_views=response.json()['data'][0]['metrics'][0]
        return page_views

    def get_users_count(self, counter_id):
        url = urljoin(self._METRIKA_STAT_URL, 'data')
        headers = self.get_header()
        params = {
                'id': counter_id,
                'metrics': 'ym:s:users'
        }
        response = requests.get(url, params,headers=headers)
        visits_count=response.json()['data'][0]['metrics'][0]
        return users_count

metrika = YandexMetrika(TOKEN)

