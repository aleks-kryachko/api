# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
53 операция добавление тел в ЛС при налиции Номера телефона и E-mail

http://jira.sibirenergo.ru/browse/AUTO-227



"""
import pytest
from conftest import server_test
import requests
import xml.etree.ElementTree as ET

server_test ='10.1.2.31'

response = requests.get(url = f'http://{server_test}/sirena/info.v15.csp?OpCode=53&BSPID=ESB&CSPID=ESS&RqUID='
                              f'&Source=nskes&AcctID=30801028&Phone=9139130123&Email=test@test_last.ru&MiddleName='
                              f'&Name=Name23&LastName=')
#  http://10.1.3.2/sirena/info.v15.csp?OpCode=53&BSPID=ESB&CSPID=ESS&RqUID=&Source=nskes&AcctID=30801028&Phone=9139130123&Email=test@test_last.ru&MiddleName=&Name=Name23&LastName=
root = ET.fromstring(response.content)
for element in root.iter('*'):         #  Вывод всех тегов
    print(element)                     #  Вывод всех тегов

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '53', 'операция на 53'

def test_check_ID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '30563058', 'Лицевой счет не 30563058'

def test_check_answer_StatText():
    for element in root.iter(tag='StatText'):
        assert element.text == 'Выполнено успешно', 'ошибка в выполнении'

def test_check_error_answer_TYPE():
    response = requests.get(url=f'http://{server_test}/sirena/info.v15.csp?OpCode=52&BSPID=ESB&CSPID=ESS&RqUID='
                                f'&Source=nskes&Phone=9139130123&Email=test@test_last.ru&MiddleName='
                                f'&Name=Name23&LastName=')
    http://10.1.3.2/sirena/info.v15.csp?OpCode=52&BSPID=ESB&CSPID=ESS&RqUID=&Source=nskes&AcctID=30801028&Phone=9139130123&Email=test@test_last.ru&MiddleName=name&Name=Name23&LastName=FIO
    root = ET.fromstring(response.content)

    for element in root.iter(tag='TYPE'):
        assert element.text == 'Ошибка информационного сервера', 'ошибка в выполнении'

def test_check_error_answer_AcctID():
    response = requests.get(url=f'http://{server_test}/sirena/info.v15.csp?OpCode=53&BSPID=ESB&CSPID=ESS&RqUID=&Source=nskes&AcctID=30801022228&Email=test@test_last.ru&MiddleName=&Name=Name23&LastName=')
    #  http://10.1.3.2/sirena/info.v15.csp?OpCode=52&BSPID=ESB&CSPID=ESS&RqUID=&Source=nskes&AcctID=30801028&Phone=9139130123&Email=test@test_last.ru&MiddleName=&Name=Name23&LastName=
    root = ET.fromstring(response.content)

    for element in root.iter(tag='StatText'):
        assert element.text == 'Ошибка при синхронизации e-mail:ERROR #00: (no error description)', 'ошибка номера ЛС'