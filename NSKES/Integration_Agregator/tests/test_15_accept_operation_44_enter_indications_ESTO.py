# -*- coding: utf-8 -*-
"""
Проверка коректного ответа агрегатора GET запроса
Ответ  XML сравниваем с эталоными значениями

Операция 44 - ввод показаний
Отделение ESTO

http://jira.sibirenergo.ru/browse/SRN-1602
http://10.1.14.13:8090/pages/viewpage.action?pageId=10726470

"""
import pytest
from conftest import server, server_ESBC, server_ESOR, server_ESTO
import requests
import xml.etree.ElementTree as ET
import datetime

response = requests.get(url = f'http://{server_ESTO}/info.v15.csp?OpCode=44&TimeStamp=2020-06-06&RPNum=1&ProductCode=1&ServiceCode=1&CustID=55764&AcctID=21235002&QValue=9999999')
#  http://10.1.4.22/sirena-toguchin/info.v15.csp?OpCode=44&TimeStamp=2020-06-06&RPNum=1&ProductCode=1&ServiceCode=1&CustID=55764&AcctID=21235002&QValue=9999999
root = ET.fromstring(response.content)


def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_OpCode():
    for element in root.iter(tag='OpCode'):
        assert element.text == '44', 'операция на 44'

def test_check_Status_5():
    for element in root.iter(tag='Status'):
        assert element.text == '0 (-3):Показания по прибору учета №35565274 на текущую дату уже есть в системе.', 'Данные не передались'

def test_check_Status_2():
    date_today = datetime.datetime.today().strftime('%Y-%m-%d')

    response = requests.get(
        url=f'http://{server_ESTO}/info.v15.csp?OpCode=44&TimeStamp={date_today}&RPNum=1&ProductCode=1&ServiceCode=1&CustID=55764&AcctID=21235002&QValue=9999999')

    root = ET.fromstring(response.content)
    for element in root.iter(tag='Status'):
        assert element.text == '0 (-2):Слишком большой расход по точке учета №1', 'Данные не передались'

