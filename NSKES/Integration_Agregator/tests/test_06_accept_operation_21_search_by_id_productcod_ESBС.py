# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 21 - поиск по Лицевому и коду продукции
Отделение ESBС проверяется на реалки т.к нет тестового Агрегатора на участках.

http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009&ProductCode=1

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server_ESBC}/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB%D0%A1&RqUID=&AcctID=200256&ProductCode=1')
#  http://10.1.4.22/sirena-chulym/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB%D0%A1&RqUID=&AcctID=200256&ProductCode=1
root = ET.fromstring(response.content)

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '21', 'операция на 21'

def test_check_CustID():
    for element in root.iter(tag='CustID'):
        assert element.text == '7356', 'Договор не 7356'

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '200256', 'Лицевой счет не 200256'

def test_check_name_city():
    for element in root.iter(tag='City'):
        assert element.text == 'ЧУЛЫМ', 'Город не ЧУЛЫМ'

def test_check_name_street():
    for element in root.iter(tag='Street'):
        assert element.text == 'ЛЕНИНА', 'Улица не ЛЕНИНА'

def test_check_number_house():
    for element in root.iter(tag='House'):
        assert element.text == '44', 'Дом не 44'

def test_check_number_flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '1', 'Квартира не 1'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1', 'ProductCode не 1'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'ProductName не Э/Энергия'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'ЧУЛЫМ', 'Район  не ЧУЛЫМ'

def test_check_OrgCode_ProductCod_3():     # ЛС 200256 OrgCode и продукция 3
    response = requests.get(
        url=f'http://{server_ESBC}/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESBC&RqUID=&AcctID=200256&ProductCode=3')
    root = ET.fromstring(response.content)
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'
    for element in root.iter(tag='OrgCode'):
        assert element.text == '65008', 'OrgCode  не 65008'

def test_check_OrgCode_ProductCod_14():     # ЛС 201543 OrgCode и продукция 3
    response = requests.get(
        url=f'http://{server_ESBC}/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESBC&RqUID=&AcctID=201543&ProductCode=14')
        #  http://10.1.4.22/sirena-chulym/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB%D0%A1&RqUID=&AcctID=201543&ProductCode=14
    root = ET.fromstring(response.content)
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'
    for element in root.iter(tag='OrgCode'):
        assert element.text == '141', 'OrgCode  не 141'

