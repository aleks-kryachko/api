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

response = requests.get(url = f'http://{server_ESOR}/info.v15.csp?OpCode=4&CSPID=TEST&RqUID=&Street=%cb%e5%ed%e8%ed%e0&House=11&Flat=13')
#  http://10.1.4.22/sirena-ordynsk/info.v15.csp?OpCode=4&CSPID=TEST&RqUID=&Street=%cb%e5%ed%e8%ed%e0&House=11&Flat=13
root = ET.fromstring(response.content)
# for element in root.iter('*'):         #  Вывод всех тегов
#     print(element)                     #  Вывод всех тегов

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '2', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '4', 'операция на 4'

def test_check_CustID():   #  Проверка Номера договора операцией 24 с сортировкой по коду продукциее
    response = requests.get(
        url=f'http://{server_ESOR}/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%cb%e5%ed%e8%ed%e0&House=11&Flat=13&ProductCode=1')
    #  http://10.1.4.22/sirena-ordynsk/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%cb%e5%ed%e8%ed%e0&House=11&Flat=13&ProductCode=1
    root = ET.fromstring(response.content)
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'
    for element in root.iter(tag='CustID'):
        assert element.text == '101000000000012408', 'Договор не 101000000000012408'

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '5005084', 'Лицевой счет не 5005084'

def test_check_City():
    for element in root.iter(tag='City'):
        assert element.text == 'Ордынское', 'Значение не Ордынское'

def test_check_Street():
    for element in root.iter(tag='Street'):
        assert element.text == 'Ленина', 'Значение не Ленина'

def test_check_House():
    for element in root.iter(tag='House'):
        assert element.text == '11', 'Значение не 11'

def test_check_Flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '13', 'Значение не 13'

def test_check_product_code():  #  Проверкакода продукции операцией 24 с сортировкой по коду продукциее
    response = requests.get(
        url=f'http://{server_ESOR}/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%cb%e5%ed%e8%ed%e0&House=11&Flat=13&ProductCode=13')
    #  http://10.1.4.22/sirena-ordynsk/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%cb%e5%ed%e8%ed%e0&House=11&Flat=13&ProductCode=13
    root = ET.fromstring(response.content)
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

    for element in root.iter(tag='ProductCode'):
        assert element.text == '13', 'ProductCode не 13'

def test_check_product_name():   #  Проверкакода продукции операцией 24 с сортировкой по коду продукциее
    response = requests.get(
        url=f'http://{server_ESOR}/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%cb%e5%ed%e8%ed%e0&House=11&Flat=13&ProductCode=1')
    #  http://10.1.4.22/sirena-ordynsk/info.v15.csp?OpCode=24&CSPID=TEST&RqUID=&Street=%cb%e5%ed%e8%ed%e0&House=11&Flat=13&ProductCode=1
    root = ET.fromstring(response.content)
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Э/Энергия', 'ProductName не Э/Энергия'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'Ордынское', 'Район  не Ордынское'