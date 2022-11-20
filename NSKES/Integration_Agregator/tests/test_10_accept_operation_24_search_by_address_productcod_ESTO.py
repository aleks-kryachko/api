# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 24 - поиск по адресу
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

response = requests.get(
        url=f'http://{server_ESTO}/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%d1%e2%e5%f0%e4%eb%ee%e2%e0&House=64&Flat=22&ProductCode=1')
    #  http://10.1.4.22/sirena-toguchin/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%d1%e2%e5%f0%e4%eb%ee%e2%e0&House=64&Flat=22&ProductCode=1
root = ET.fromstring(response.content)

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '24', 'операция на 24'

def test_check_CustID():
    for element in root.iter(tag='CustID'):
        assert element.text == '34014', 'Договор не 34014'

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '256971', 'Значение не 256971'

def test_check_City():
    for element in root.iter(tag='City'):
        assert element.text == 'ТОГУЧИН', 'Значение не ТОГУЧИН'

def test_check_Street():
    for element in root.iter(tag='Street'):
        assert element.text == 'СВЕРДЛОВА', 'Значение не СВЕРДЛОВА'

def test_check_House():
    for element in root.iter(tag='House'):
        assert element.text == '64', 'Значение не 64'

def test_check_Flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '22', 'Значение не 22'

def test_check_ProductCode():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '1', 'Значение не 1'

def test_check_ProductName():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'Значение не Э/Энергия'

def test_check_ProductCode_13():
    response = requests.get(
        url=f'http://{server_ESTO}/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%d1%e2%e5%f0%e4%eb%ee%e2%e0&House=62&Flat=8&ProductCode=13')
    root = ET.fromstring(response.content)
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'
    for element in root.iter(tag='ProductCode'):
        assert element.text == '13', 'Значение не 1'

def test_check_ProductName_13():
    response = requests.get(
        url=f'http://{server_ESTO}/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%d1%e2%e5%f0%e4%eb%ee%e2%e0&House=62&Flat=8&ProductCode=13')
    root = ET.fromstring(response.content)
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Общедомовые нужды (э/э)', 'Значение не Общедомовые нужды (э/э)'