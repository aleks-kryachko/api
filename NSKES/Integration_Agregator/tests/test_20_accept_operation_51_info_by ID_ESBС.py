# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 51 - информация по договору
Отделение ESBС

http://jira.sibirenergo.ru/browse/SRN-1602
http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET

response = requests.get(url = f'http://{server_ESBC}/info.v15.csp?OpCode=51&CSPID=TEST&BSPID=ESB%D0%A1&RqUID=&CustID=20026')
#  http://10.1.4.22/sirena-chulym/info.v15.csp?OpCode=51&CSPID=TEST&BSPID=ESB%D0%A1&RqUID=&CustID=20026
root = ET.fromstring(response.content)


def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '51', 'операция на 51'

def test_check_ID():
    for element in root.iter(tag='CustID'):
        assert element.text == '20026', 'Лицевой счет не 20026'

def test_check_product_code():
    for element in root.iter(tag='ProductCode'):
        assert element.text == '7', 'ProductCode не 7'

def test_check_product_name():
    for element in root.iter(tag='ProductName'):
        assert element.text == 'Дополнительные услуги Новосибиркэнергосбыт', 'ProductName неДополнительные услуги Новосибиркэнергосбыт'

def test_check_ServName():
    for element in root.iter(tag='ServName'):
        assert element.text == 'Вызов монтера ЦЭС,доп.услуги НЭС', 'ответ не Вызов монтера ЦЭС,доп.услуги НЭС'

def test_check_ProdNamePrint():
    for element in root.iter(tag='ProdNamePrint'):
        assert element.text == 'Дополнительные услуги', 'ответ не Дополнительные услуги'

def test_check_SumDServ():
    for element in root.iter(tag='SumDServ'):
        assert element.text != None, 'ответ Taxa не 0'

def test_check_SumDProd():
    for element in root.iter(tag='SumDProd'):
        assert element.text != None, 'ответ Taxa не 0'

def test_check_CalcSum():
    for element in root.iter(tag='CalcSum'):
        assert element.text != None, 'ответ CalcSum не 2.68'

def test_check_PrevMonth():
    for element in root.iter(tag='PrevMonth'):
        assert element.text != None, 'ответ PrevMonth не июнь 2020'



