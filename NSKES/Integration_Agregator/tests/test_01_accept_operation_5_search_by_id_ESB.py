# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 5 - поиск по ID договора
Отделение ESB проверяется на реалки т.к нет тестового Агрегатора на участках.

http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=5&CSPID=TEST&BSPID=ESB&RqUID=&CustID=17 - Поиск по номеру договора

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server}/sirena/info.v15.csp?OpCode=5&CSPID=TEST&BSPID=ESB&RqUID=&CustID=2327549')
#  http://10.1.3.2/sirena/info.v15.csp?OpCode=5&CSPID=TEST&BSPID=ESB&RqUID=&CustID=2327546
root = ET.fromstring(response.content)

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '5', 'операция на 51'

def test_check_CustID():
    for element in root.iter(tag='CustID'):
        assert element.text == '2327549', 'Договор не 2327549'

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '30563061', 'Лицевой счет не 30563061'

def test_check_name_city():
    for element in root.iter(tag='City'):
        assert element.text == 'НОВОСИБИРСК', 'Город не НОВОСИБИРСК'

def test_check_name_street():
    for element in root.iter(tag='Street'):
        assert element.text == 'МЯСНИКОВОЙ УЛ.', 'Улица не МЯСНИКОВОЙ УЛ.'

def test_check_number_house():
    for element in root.iter(tag='House'):
        assert element.text == '30', 'Дом не 30'

def test_check_number_flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '61', 'Квартира не 61'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1', 'ProductCode не 1'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'ProductName не Э/Энергия'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'КАЛИНИНСКИЙ', 'Район  не КАЛИНИНСКИЙ'

