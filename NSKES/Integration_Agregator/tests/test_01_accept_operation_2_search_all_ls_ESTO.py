# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 2 - поиск по началу лицевому счету, адреса и продукции
Отделение ESTO проверяется на реалки т.к нет тестового Агрегатора на участках.

http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=2&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=3080100 -все лицевые начинающиеся с 3080100

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

customers_etalon = ['404310', '404311', '404312', '404313', '404314', '404315', '404316', '404317', '404318', '404319']

response = requests.get(url = f'http://{server_ESTO}/info.v15.csp?OpCode=2&CSPID=TEST&BSPID=ESTO&RqUID=&AcctID=40431')
#  http://10.1.4.22/sirena-toguchin/info.v15.csp?OpCode=2&CSPID=TEST&BSPID=ESTO&RqUID=&AcctID=40431
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

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        print(element.text)
        assert element.text in customers_etalon, 'Лицевого номера нет, в списке'

def test_check_name_city():
    for element in root.iter(tag='City'):
        assert element.text == 'ТОГУЧИН', 'Город не соответствует'

def test_check_name_street():
    for element in root.iter(tag='Street'):
        assert element.text == 'ЛЕНИНА' or element.text == 'Первомайская', 'Улица соответствует'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1' or element.text == '13', 'ProductCode не соответствует'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия' or element.text == 'Общедомовые нужды (э/э)', 'ProductName несоответствует'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'Тогучин', 'Район  не соответствует'
