# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 45 - расчет показаний

http://jira.sibirenergo.ru/browse/SRN-1602
http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET
import datetime

response = requests.get(url = f'http://{server}/sirena/info.v15.csp?OpCode=45&CSPID=TEST&BSPID=ESB&RqUID=&CustID=230995&ProductCode=1&ServiceCode=1&CDate=2020-05-30&OpType=3&Param=30853&RPNum=1')
#  http://10.0.0.202/sirena/info.v15.csp?OpCode=45&CSPID=TEST&BSPID=ESB&RqUID=&CustID=230995&ProductCode=1&ServiceCode=1&CDate=2020-05-30&OpType=3&Param=30853&RPNum=1
root = ET.fromstring(response.content)


def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '45', 'операция на 44'

def test_check_Sum():
    for element in root.iter(tag='Sum'):
        assert element.text != None, 'Значение не коректное'

def test_check_PayLine():
    for element in root.iter(tag='PayLine'):
        assert element.text != None, 'Значение не коректное'

def test_check_NameSumAdvs():
    for element in root.iter(tag='NameSumAdvs'):
        assert element.text == 'скидка по льготе', 'Значение не коректное'

def test_check_SumAdvs():
    for element in root.iter(tag='SumAdvs'):
        assert element.text != None, 'Значение не коректное'

def test_check_NameSumSubs():
    for element in root.iter(tag='NameSumSubs'):
        assert element.text == 'скидка по субсидии', 'Значение не коректное'

def test_check_SumSubs():
    for element in root.iter(tag='SumSubs'):
        assert element.text != None, 'Значение не коректное'

def test_check_NameSumReCalc():
    for element in root.iter(tag='NameSumReCalc'):
        assert element.text == 'перерасчет', 'Значение не коректное'

def test_check_SumReCalc():
    for element in root.iter(tag='SumReCalc'):
        assert element.text != None, 'Значение не коректное'

def test_check_P1():
    for element in root.iter(tag='P1'):
        assert element.text == '89105', 'Значение не коректное'
