"""
Разноска оперативного платежа
по Электичеству
Проверять на ТЕСТЕ server_test
"""

import pytest
from conftest import server_test
import requests
import xml.etree.ElementTree as ET

date_pyment = '2020-09-10'
CustID ='2139412'     #   Номер договора
AcctID ='10370140'  #   Номер ЛС
Sum ='331'

response = requests.get(url = f'http://{server_test}/sirena/csp.info.v15.cls?OpCode=30&TimeStamp={date_pyment}&OpType=3&CSPDivision=TEST&ProductCode=1&ServiceCode=1&CustID={CustID}&AcctID={AcctID}&CDate={date_pyment}&QValue=1&Sum={Sum}&RPNum=1&OpID=111&TerminalID=222')
#  http://10.1.2.31/sirena/csp.info.v15.cls?OpCode=30&TimeStamp=2020-09-02&OpType=3&CSPDivision=TEST&ProductCode=1&ServiceCode=1&CustID=402121&AcctID= 601450172&CDate=2020-09-02&QValue=10010&Sum=100&RPNum=1&OpID=111&TerminalID=222
root = ET.fromstring(response.content)

def test_check_status_cod():
    assert response.status_code == 200, 'Статус не 200'

def test_check_status_count():
    for element in root.iter(tag='Count'):
        assert element.text == '1', 'Нет информации для вывода. Ответ Пуст'

def test_check_Status():
    for element in root.iter(tag='Status'):
        assert element.text == '1', 'Платеж не прошел'