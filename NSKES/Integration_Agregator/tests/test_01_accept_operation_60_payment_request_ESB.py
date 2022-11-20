# -*- coding: utf-8 -*-
"""
------  Ответ от Агрегатора -- Нужно от СИРЕНЫ !!!!


Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 60 - Запрос платежно документа
Отделение ESB

http://jira.sibirenergo.ru/browse/SRN-1602
http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://10.2.1.11/csp/router/Services.Report.cls?CSPID=TEST&BSPID=ESB&OpCode=60&RqUID=1&AcctID=30801027&ProdList=13')
#  http://10.2.1.11/csp/router/Services.Report.cls?CSPID=TEST&BSPID=ESB&OpCode=60&RqUID=1&AcctID=30801027&ProdList=13
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
        assert element.text == '60', 'операция не 60'

def test_check_Status():
    for element in root.iter(tag='Status'):
        assert element.text == '1', 'операция не 1'

def test_check_StatusText():
    for element in root.iter(tag='StatusText'):
        assert element.text == 'OK', 'операция не OK'

def test_check_Document():
    for element in root.iter(tag='Document'):
        assert element.text != None, 'Содержимое пусто'