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
from conftest import server, server_ESOR
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server_ESOR}/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESOR&RqUID=&AcctID=5005009')
#  http://10.1.4.22/sirena-ordynsk/info.v15.csp?OpCode=5&CSPID=TEST&BSPID=ESOR&RqUID=&CustID=24359
root = ET.fromstring(response.content)
for element in root.iter('*'):         #  Вывод всех тегов
    print(element)                     #  Вывод всех тегов

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '2', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '1', 'операция на 1'

def test_check_ID():
    for element in root.iter(tag='AcctID'):
        print(element.text)
        assert element.text == '5005009', 'Лицевой счет не 5005009'

def test_check_name_city():
    for element in root.iter(tag='City'):
        assert element.text == 'Ордынское', 'Город не Ордынское'

def test_check_name_street():
    for element in root.iter(tag='Street'):
        assert element.text == 'Ленина', 'Улица не Ленина'

def test_check_number_house():
    for element in root.iter(tag='House'):
        assert element.text == '5', 'Дом не 5'

def test_check_number_flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '6', 'Квартира не 6'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '13', 'ProductCode не 13'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Общедомовые нужды (э/э)', 'ProductName не Общедомовые нужды (э/э)'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'Ордынское', 'Район  не Ордынское'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1' or '13', 'ProductCode не 1'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия' or 'Общедомовые нужды (э/э)', 'ProductName не Э/Энергия'
