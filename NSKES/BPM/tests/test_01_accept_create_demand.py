# -*- coding: utf-8 -*-
"""
Тестирование создание заявки на доп.услуги из БПМ
запрося из нагрузочного тестирования http://jira.sibirenergo.ru/browse/TEST-139?src=confmacro
http://10.1.14.13:8090/pages/viewpage.action?pageId=2000245

Тест без плановой даты Новосибирск
Тест с плановой датой Новосибирск
Тест создание на участе ESTO
Тест создание на участке ESOR
Тест создание на участке ESBC
Тест на ошибку при создании заявки
"""
import pytest
import requests
import datetime
from datetime import date
from conftest import server_ESOR,server_ESTA,server_ESBS,server_ESTO, server_test, server_test_ESBC,server_test_ESOR
from conftest import server_test_ESTO, server_test_ESBI, server_test_ESBY, server_test_ESBB, server_test_ESCH
from conftest import server_test_ESTA
import json

#  ЛС без ДУ 30801024 договор 17   ТУ 101000000001041681
#            30807028 договор 719   ТУ 101000000000958002
server_test = '10.1.2.83/sirena'
date = date.today()
url = f'http://{server_test}/bpmservice/createDemand'
# http://10.1.2.83/bpmservice/createDemand
# Создание заявки без плановой даты
def test_01_without_plandate():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        {
            "DocDate": str(date), "ContractGlobalId":"sirena\\Contracts.EPhDogovor\\ESB\\17",   #ЛС 30801024
            "DepartmentCode":2,
            "ServiceIds":[219],
            "Notes":"only English words",
            "Contact1":{"Phone":"9231254282", "Fio":"Petrov Peter123"},
            "Contact2":{"Phone":"9231254281", "Fio":"Ivanov Vasil Borisovich"},
            "NotifyMethod":"Call after 1 hour",
            "PayOnHome": False,
            "RegPointGlobalId":"sirena\\RegPoints.ERegPoint\\ESB\\101000000001041681",
            "DisplayFio": True,
            "PlanDate": ""
        }
    )
    print(response.status_code, response.json())
    answer = response.json()
    assert response.status_code == 200, 'Ответа от сервера нет'
    assert answer['data'] != None, ''
    assert answer['message'] == 'Сохранено','Заявка на ДУ не сохранилась'
    assert answer['status'] == '0', 'Ошибка'

# Создание заявки с плановой датой
def test_02_with_plandate():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        {
            "DocDate":str(date), "ContractGlobalId":"sirena\\Contracts.EPhDogovor\\ESB\\719",  # ЛС 30807028
            "DepartmentCode":2,
            "ServiceIds":[221],
            "Notes":"only English words",
            "Contact1":{"Phone":"123456789", "Fio":"Test Testovich - 123"},
            "Contact2":{"Phone":"987654321", "Fio":"Testovich Tester - 456"},
            "NotifyMethod":"Call after 1 hour",
            "PayOnHome": False,
            "RegPointGlobalId":"sirena\\RegPoints.ERegPoint\\ESB\\101000000000958002",
            "DisplayFio": True,
            "PlanDate": str(date)
        }
    )
    print(response.status_code, response.json())
    answer = response.json()
    assert response.status_code == 200, 'Ответа от сервера нет'
    assert answer['data'] != None, ''
    assert answer['message'] == 'Сохранено', 'Заявка на ДУ не сохранилась'
    assert answer['status'] == '0', 'Ошибка'

# Создание заявки на участке ESTO
def test_03_ESTO():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        {
            "DocDate":str(date), "ContractGlobalId":"sirena\\Contracts.EPhDogovor\\ESTO\\55778",  # ЛС 404314
            "DepartmentCode":2,
            "ServiceIds":[221],
            "Notes":"only English words",
            "Contact1":{"Phone":"123456789", "Fio":"Test Testovich - 123"},
            "Contact2":{"Phone":"987654321", "Fio":"Testovich Tester - 456"},
            "NotifyMethod":"Call after 1 hour",
            "PayOnHome": False,
            "RegPointGlobalId":"sirena\\RegPoints.ERegPoint\\ESB\\307000000000042152",
            "DisplayFio": True,
            "PlanDate": str(date)
        }
    )
    print(response.status_code, response.json())
    answer = response.json()
    assert response.status_code == 200, 'Ответа от сервера нет'
    assert answer['data'] != None, ''
    assert answer['message'] == 'Сохранено', 'Заявка на ДУ не сохранилась'
    assert answer['status'] == '0', 'Ошибка'

# Создание заявки на участке ESOR
def test_04_ESOR():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        {
            "DocDate":str(date), "ContractGlobalId":"sirena\\Contracts.EPhDogovor\\ESOR\\101000000000012344",  # ЛС 5005010
            "DepartmentCode":2,
            "ServiceIds":[221],
            "Notes":"only English words",
            "Contact1":{"Phone":"123456789", "Fio":"Test Testovich - 123"},
            "Contact2":{"Phone":"987654321", "Fio":"Testovich Tester - 456"},
            "NotifyMethod":"Call after 1 hour",
            "PayOnHome": False,
            "RegPointGlobalId":"sirena\\RegPoints.ERegPoint\\ESB\\307000000000012740",
            "DisplayFio": True,
            "PlanDate": str(date)
        }
    )
    print(response.status_code, response.json())
    answer = response.json()
    assert response.status_code == 200, 'Ответа от сервера нет'
    assert answer['data'] != None, ''
    assert answer['message'] == 'Сохранено', 'Заявка на ДУ не сохранилась'
    assert answer['status'] == '0', 'Ошибка'

# Создание заявки на участке ESBC
def test_05_ESBC():
    url = f'http://{server_test}/bpmservice/createDemand'
    # http://10.1.2.83/sirena-chulym/bpmservice/createDemand
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        {
            "DocDate":str(date), "ContractGlobalId":"sirena\\Contracts.EPhDogovor\\ESBC\\7324",  # ЛС 200214
            "DepartmentCode":2,
            "ServiceIds":[221],
            "Notes":"only English words",
            "Contact1":{"Phone":"123456789", "Fio":"Test Testovich - 123"},
            "Contact2":{"Phone":"987654321", "Fio":"Testovich Tester - 456"},
            "NotifyMethod":"Call after 1 hour",
            "PayOnHome": False,
            "RegPointGlobalId":"sirena\\RegPoints.ERegPoint\\ESB\\101000000000002067",
            "DisplayFio": True,
            "PlanDate": str(date)
        }
    )
    print(response.status_code, response.json())
    answer = response.json()
    assert response.status_code == 200, 'Ответа от сервера нет'
    assert answer['data'] != None, ''
    assert answer['message'] == 'Сохранено', 'Заявка на ДУ не сохранилась'
    assert answer['status'] == '0', 'Ошибка'

# Создание заявки с ошибкой 'Ошибка создания:Ошибка поиска типа документа!'
def test_06_Error():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        {
            "DocDate": str(date), "ContractGlobalId":"sirena\\Contracts.EPhDogovor\\ESB\\",
            "DepartmentCode":2,
            "ServiceIds":[219],
            "Notes":"only English words",
            "Contact1":{"Phone":"9231254282", "Fio":"Petrov Peter123"},
            "Contact2":{"Phone":"9231254281", "Fio":"Ivanov Vasil Borisovich"},
            "NotifyMethod":"Call after 1 hour",
            "PayOnHome": False,
            "RegPointGlobalId":"sirena\\RegPoints.ERegPoint\\ESB\\101000000001041681",
            "DisplayFio": True,
            "PlanDate": ""
        }
    )
    print(response.status_code, response.json())
    answer = response.json()
    assert answer['data'] != "{'contractId': None, 'orderId': None}", 'Метод сломан'
    assert answer['message'] == 'Ошибка создания:Ошибка поиска типа документа!', 'Метод Сломан'
    assert answer['status'] == '1', 'Метод сломан'
