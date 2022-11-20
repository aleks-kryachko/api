# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 1 - поиск по лицевому счету, адреса и продукции
Отделение ESB

http://jira.sibirenergo.ru/browse/SRN-1602
http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009 - поиск по лицевому

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server}/sirena/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30563058')
#  http://10.0.0.202/sirena/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009
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
        assert element.text == '30563058', 'Лицевой счет не 30563058'

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
        assert element.text == '58', 'Квартира не 58'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1', 'ProductCode не 1'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'ProductName не Э/Энергия'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'КАЛИНИНСКИЙ', 'Район  не КАЛИНИНСКИЙ'

def test_check_OrgCode():     # ЛС 20115099 бездоговорное потребление
    response = requests.get(
        url=f'http://{server}/sirena/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=20115099')
        #  http://10.0.0.202/sirena/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=61023011
    root = ET.fromstring(response.content)
    for element in root.iter(tag='OrgCode'):
        assert element.text == '141', 'OrgCode  не 141'


