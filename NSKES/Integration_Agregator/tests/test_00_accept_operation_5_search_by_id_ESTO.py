# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 5 - поиск по ID договора
Отделение ESTO проверяется на реалки т.к нет тестового Агрегатора на участках.

http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=5&CSPID=TEST&BSPID=ESB&RqUID=&CustID=17 - Поиск по номеру договора

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server_ESTO}/info.v15.csp?OpCode=5&CSPID=TEST&BSPID=ESTO&RqUID=&CustID=55764')
#  http://10.1.4.22/sirena-toguchin/info.v15.csp?OpCode=5&CSPID=TEST&BSPID=ESTO&RqUID=&CustID=55764
root = ET.fromstring(response.content)

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '5', 'операция на 5'

def test_check_CustID():
    for element in root.iter(tag='CustID'):
        assert element.text == '55764', 'Договор не 55764'

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '21235002', 'Лицевой счет не 21235002'

def test_check_name_city():
    for element in root.iter(tag='City'):
        assert element.text == 'ГОРНЫЙ', 'Город не ГОРНЫЙ'

def test_check_name_street():
    for element in root.iter(tag='Street'):
        assert element.text == 'Карьерная', 'Улица не Карьерная'

def test_check_number_house():
    for element in root.iter(tag='House'):
        assert element.text == '35/2', 'Дом не 35/2'

def test_check_number_flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '0', 'Квартира не 0'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1', 'ProductCode не 1'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'ProductName не Э/Энергия'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'Горный', 'Район  не Горный'

