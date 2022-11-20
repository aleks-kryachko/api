# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 21 - поиск по Лицевому и коду продукции

http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470
http://10.1.3.2/sirena/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESB&RqUID=&AcctID=30801009&ProductCode=1

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO, server_ESBI
import requests
import xml.etree.ElementTree as ET

response = requests.get(
        url=f'http://{server_ESBI}/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESBI%D0%A1&RqUID=&AcctID=931223489&ProductCode=6')
        #  http://10.1.4.22/sirena-berdsk/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESTO%D0%A1&RqUID=&AcctID=931223489&ProductCode=6
root = ET.fromstring(response.content)

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '21', 'операция на 21'

def test_check_OrgCode_ProductCod_6():     # ЛС 931223489 OrgCode и продукция 6
    for element in root.iter(tag='OrgCode'):
        assert element.text == '141', 'OrgCode  не 141'

def test_check_OrgCode_ProductCod_14():     # ЛС 931027230 OrgCode и продукция 14
    response = requests.get(
        url=f'http://{server_ESBI}/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESBI%D0%A1&RqUID=&AcctID=931017625&ProductCode=14')
        #  http://10.1.4.22/sirena-berdsk/info.v15.csp?OpCode=21&CSPID=TEST&BSPID=ESBI%D0%A1&RqUID=&AcctID=931017625&ProductCode=14
    root = ET.fromstring(response.content)
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'
    for element in root.iter(tag='OrgCode'):
        assert element.text == '141', 'OrgCode  не 141'

