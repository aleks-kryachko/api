# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 4 - поиск по адресу
Для конвертации текста в шестнадцатеричный код , можно использовать конвертер Text To Hex / Hex To Text
http://crypt-online.ru/crypts/text2hex/
http://10.0.0.202/sirena/info.v15.csp?OpCode=4&CSPID=TEST&BSPID=ESB&RqUID=&Street=%c3%ee%e3%ee%eb%ff&House=1&Flat=27
(Гоголя 1-27)

http://jira.sibirenergo.ru/browse/SRN-1602
http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=1&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009 - поиск по лицевому

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server}/sirena/info.v15.csp?OpCode=4&CSPID=TEST&BSPID=ESB&RqUID=&Street=%D1%F2%F3%E4%E5%ED%F7%E5%F1%EA%E0%FF&House=67')
#  http://10.0.0.202/sirena/info.v15.csp?OpCode=4&CSPID=TEST&BSPID=ESB&RqUID=&Street=%D1%F2%F3%E4%E5%ED%F7%E5%F1%EA%E0%FF&House=67
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
        assert element.text == '4', 'операция на 4'

def test_check_CustID():
    for element in root.iter(tag='CustID'):
        assert element.text == '35', 'Договор не 35'

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '30801042', 'Лицевой счет не 30801042'

def test_check_City():
    for element in root.iter(tag='City'):
        assert element.text == 'НОВОСИБИРСК', 'Значение не НОВОСИБИРСК'

def test_check_Street():
    for element in root.iter(tag='Street'):
        assert element.text == 'СТУДЕНЧЕСКАЯ УЛ.', 'Значение не СТУДЕНЧЕСКАЯ УЛ.'

def test_check_House():
    for element in root.iter(tag='House'):
        assert element.text == '67', 'Значение не 67'

def test_check_Flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '0', 'Значение не 0'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1', 'ProductCode не 1'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'ProductName не Э/Энергия'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'ЗАЕЛЬЦОВСКИЙ', 'Район  не ЗАЕЛЬЦОВСКИЙ'

