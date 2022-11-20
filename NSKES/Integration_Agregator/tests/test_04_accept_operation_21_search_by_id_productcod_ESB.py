# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 21 - поиск по Лицевому и коду продукции
Отделение ESB проверяется на реалки т.к нет тестового Агрегатора на участках.

http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009&ProductCode=1

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server}/sirena/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009&ProductCode=1')
#  http://10.1.3.2/sirena/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009&ProductCode=1
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
        assert element.text == '6', 'Договор не 6'

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '30801009', 'Лицевой счет не 30801009'

def test_check_name_city():
    for element in root.iter(tag='City'):
        assert element.text == 'НОВОСИБИРСК', 'Город не НОВОСИБИРСК'

def test_check_name_street():
    for element in root.iter(tag='Street'):
        assert element.text == 'СТУДЕНЧЕСКАЯ УЛ.', 'Улица не СТУДЕНЧЕСКАЯ УЛ.'

def test_check_number_house():
    for element in root.iter(tag='House'):
        assert element.text == '50 А', 'Дом не 50 А'

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
        assert element.text == 'ЗАЕЛЬЦОВСКИЙ', 'Район  не ЗАЕЛЬЦОВСКИЙ'

def test_check_OrgCode_ProductCode_14():     # ЛС 40125117 OrgCode и продукция 14
    response = requests.get(
        url=f'http://{server}/sirena/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=40125117&ProductCode=14')
    root = ET.fromstring(response.content)
    for element in root.iter(tag='OrgCode'):
        assert element.text == '141', 'OrgCode  не 141'

def test_check_OrgCode_ProductCode_6():     # ЛС 20115097 OrgCode и продукция 6
    response = requests.get(
        url=f'http://{server}/sirena/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=61023011&ProductCode=6')
        # http://10.0.0.202/sirena/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=61023011&ProductCode=6
    root = ET.fromstring(response.content)
    for element in root.iter(tag='OrgCode'):
        assert element.text == '141', 'OrgCode  не 141'