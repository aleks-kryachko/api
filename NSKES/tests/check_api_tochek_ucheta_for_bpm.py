"""
задача SRN-1262

Тестирование API - выдачу полей в Json для Точек Учета

Автотест задачи SRN-1262 проверка на количество обьектов в JSON.
1 тест Проверяем договор с 1 объектом (договор 730162)
2 тест Проверяем договор с 2 объектом (договор 229623)
3 тест Проверяем договор с 3 объектом (договор 1811074)
4 тест Проверяем договор с 0 объектом, нет точки учета (договор 2076016)
"""
import pytest
import requests
import json

session = requests.Session()
headers = {'login_username': 'bpm',
           'login_password': 'bpm1'}

def test_01_check_object_length():
    url = 'http://10.1.2.31:57772/sirena/bpmservice/getTUList?contractId=sirena\\Contracts.EPhDogovor\\ESB\\730162'
    response = session.get(url=url, auth=(headers['login_username'], headers['login_password']))
    object_length = (len(response.json()))
    assert object_length == 1

def test_02_check_object_length():
    url = 'http://10.1.2.31:57772/sirena/bpmservice/getTUList?contractId=sirena\\Contracts.EPhDogovor\\ESB\\229623'
    response = session.get(url=url, auth=(headers['login_username'], headers['login_password']))
    object_length = (len(response.json()))
    assert object_length == 2

def test_03_check_object_length():
    url = 'http://10.1.2.31:57772/sirena/bpmservice/getTUList?contractId=sirena\\Contracts.EPhDogovor\\ESB\\1811074'
    response = session.get(url=url, auth=(headers['login_username'], headers['login_password']))
    object_length = (len(response.json()))
    assert object_length == 3

def test_04_check_object_length():
    url = 'http://10.1.2.31:57772/sirena/bpmservice/getTUList?contractId=sirena\\Contracts.EPhDogovor\\ESB\\2076016'
    response = session.get(url=url, auth=(headers['login_username'], headers['login_password']))
    object_length = (len(response.json()))
    assert object_length == 0
