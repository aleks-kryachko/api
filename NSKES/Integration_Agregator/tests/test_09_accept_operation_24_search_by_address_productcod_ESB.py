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

response = requests.get(url = f'http://{server}/sirena/info.v15.csp?OpCode=24&CSPID=TEST&BSPID=ESB&RqUID=&Street=%ca%d3%c1%ce%c2%c0%df&House=106&Flat=8&ProductCode=14')
#  http://10.0.0.202/sirena/info.v15.csp?OpCode=24&CSPID=TEST&BSPID=ESB&RqUID=&Street=%ca%d3%c1%ce%c2%c0%df&House=106&Flat=8&ProductCode=14
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
        assert element.text == '24', 'операция на 24'

def test_check_CustID():
    for element in root.iter(tag='CustID'):
        assert element.text == '2024070', 'Договор не 2024070'

def test_check_AcctID():
    for element in root.iter(tag='AcctID'):
        assert element.text == '30550008', 'Лицевой счет не 30550008'

def test_check_City():
    for element in root.iter(tag='City'):
        assert element.text == 'НОВОСИБИРСК', 'Значение не НОВОСИБИРСК'

def test_check_Street():
    for element in root.iter(tag='Street'):
        assert element.text == 'КУБОВАЯ УЛ.', 'Значение не КУБОВАЯ УЛ.'

def test_check_House():
    for element in root.iter(tag='House'):
        assert element.text == '106', 'Значение не 106'

def test_check_Flat():
    for element in root.iter(tag='Flat'):
        assert element.text == '8', 'Значение не 8'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '14', 'ProductCode не 14'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Общедомовые приборы учета электроэнергии', 'ProductName не Общедомовые приборы учета электроэнергии'

def test_check_city_aria():
    for element in root.iter(tag='Settle'):
        assert element.text == 'ЗАЕЛЬЦОВСКИЙ', 'Район  не ЗАЕЛЬЦОВСКИЙ'

