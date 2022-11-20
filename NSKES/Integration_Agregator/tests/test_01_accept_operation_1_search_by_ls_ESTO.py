# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 1 - поиск по лицевому счету, адреса и продукции
Отделение ESTO проверяется на реалки т.к нет тестового Агрегатора на участках.

http://jira.sibirenergo.ru/browse/SRN-1602
http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009 - поиск по лицевому

"""
import pytest
from conftest import server, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server_ESTO}/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESTO&RqUID=&AcctID=404311')
#  http://10.1.4.22/sirena-toguchin/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESTO&RqUID=&AcctID=404311
root = ET.fromstring(response.content)
# for element in root.iter('*'):         #  Вывод всех тегов
#     print(element)                     #  Вывод всех тегов

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '1', 'операция на 1'

def test_check_ID():
    for element in root.iter(tag='AcctID'):
        print(element.text)
        assert element.text == '404311', 'Лицевой счет не 404311'

def test_check_name_city():
    for element in root.iter(tag='City'):
        assert element.text == 'ТОГУЧИН', 'Город не ТОГУЧИН'

def test_check_name_street():
    for element in root.iter(tag='Street'):
        assert element.text == 'ЛЕНИНА', 'Улица не ЛЕНИНА'

def test_check_number_house():
    for element in root.iter(tag='House'):
        assert element.text == '4/3', 'Дом не 4/3'

def test_check_number_flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '11', 'Квартира не 11'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1', 'ProductCode не 1'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'ProductName не Э/Энергия'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'Тогучин', 'Район  не Тогучин'

