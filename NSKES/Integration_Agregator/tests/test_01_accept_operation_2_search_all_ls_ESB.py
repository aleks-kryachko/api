# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 2 - поиск по началу лицевому счету, адреса и продукции

http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=2&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=3080100 -все лицевые начинающиеся с 3080100

"""
import pytest
from conftest import server
import requests
import xml.etree.ElementTree as ET

customers_etalon = ['30563050', '30563051', '30563052', '30563053', '30563054',
                    '30563055', '30563056', '30563057', '30563058', '30563059']

response = requests.get(url = f'http://{server}/sirena/info.v15.csp?OpCode=2&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=3056305')
#  http://10.1.3.2/sirena/info.v15.csp?OpCode=2&CSPID=TEST&RqUID=&AcctID=3056305
root = ET.fromstring(response.content)
# for element in root.iter('*'):         #  Вывод всех тегов
#     print(element)                     #  Вывод всех тегов

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_Count():
    for element in root.iter(tag='Count'):
        assert element.text == '10', 'Количество записей не соответствует'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '2', 'операция на 2'

def test_check_Customers():
    for element in root.iter(tag='AcctID'):
        print(element.text)
        assert element.text in customers_etalon, 'Лицевого номера нет, в списке'

def test_check_name_city():
    for element in root.iter(tag='City'):
        assert element.text == 'НОВОСИБИРСК', 'Город не НОВОСИБИРСК'

def test_check_name_street():
    for element in root.iter(tag='Street'):
        assert element.text == 'МЯСНИКОВОЙ УЛ.', 'Улица не МЯСНИКОВОЙ УЛ.'

def test_check_number_house():
    for element in root.iter(tag='House'):
        assert element.text == '30', 'Дом не 30'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1', 'ProductCode не 1'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'ProductName не Э/Энергия'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'КАЛИНИНСКИЙ', 'Район  не КАЛИНИНСКИЙ'
