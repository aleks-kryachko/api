# -*- coding: utf-8 -*-
"""
Проверка метода sirena/bpmservice/FindAddress
поиск ЛС, Договоров,продукции по адресу.

http://jira.sibirenergo.ru/browse/SRN-1956
http://confluence.sibirenergo.ru/pages/viewpage.action?pageId=26884173

"""
import requests
import json
from conftest import server_ESOR,server_ESTA,server_ESBS,server_ESTO, bspids, server

server = '10.1.2.83/sirena'
url = f'http://{server}/api/service/FindFnumPersonInform'
# Проверка работы метода когда все ОК
def test_01_status200():

    data={"lastname":"МАНАЕНКОВ",
          "name": "ВАСИЛИЙ",
          "midlname": "ИВАНОВИЧ",
          "bspid":"ESB",
          "city": "НОВОСИБИРСК",
          "street": "СТУДЕНЧЕСКАЯ УЛ.",
          "house": "60",
          "flat": "0",
          "phone":"9137310075"}

    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=data)
    answer = response.json()
    print(answer)
    assert response.status_code == 200, 'Сервер не отвечает'
# Проверка работы метода когда Error
def test_02_answerErr():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        { "lastname":"МАНАЕНКОВ",
          "name": "ВАСИЛИЙ",
          "midlname": "ИВАНОВИЧ",
          "bspid":"ESB",
          "city": "НОВОСИБИРСК",
          "street": "СТУДЕНЧЕСКАЯ УЛ.",
          "house": "60",
          "flat": "0",
          "phone": "9137310075"
        }
    )
    answer = response.json()

    assert answer['Status'] == 'Err', 'Статус не Err'

# Проверка работы метода когда Error
def test_03_answerErr():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        { "lastname":"",
          "name": "ВАСИЛИЙ",
          "midlname": "ИВАНОВИЧ",
          "bspid":"ESB",
          "city": "НОВОСИБИРСК",
          "street": "СТУДЕНЧЕСКАЯ УЛ.",
          "house": "60",
          "flat": "0",
          "phone": "9137310075"
        }
    )
    answer = response.json()

    assert answer['Status'] == 'Err', 'Статус не Err'

# Проверка работы метода когда Error
def test_04_answerErr():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        { "lastname":"МАНАЕНКОВ",
          "name": "Й",
          "midlname": "ИВАНОВИЧ",
          "bspid":"ESB",
          "city": "НОВОСИБИРСК",
          "street": "СТУДЕНЧЕСКАЯ УЛ.",
          "house": "60",
          "flat": "0",
          "phone": "9137310075"
        }
    )
    answer = response.json()

    assert answer['Status'] == 'Err', 'Статус не Err'

# Проверка работы метода когда Error
def test_05_answerErr():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        { "lastname":"МАНАЕНКОВ",
          "name": "ВАСИЛИЙ",
          "midlname": "ИВАНОВИЧ",
          "bspid":"ESB",
          "city": "НОВОСИБИРСК",
          "street": "СТУДЕНЧЕСКАЯ УЛ.",
          "house": "60",
          "flat": "0",
          "phone": ""
        }
    )
    answer = response.json()

    assert answer['Status'] == 'Err', 'Статус не Err'

# Проверка работы метода когда Error
def test_06_answerErr():
    json ={"lastname": "МАНАЕНКОВ",
         "name": "ВАСИЛИЙ",
        "midlname": "ИВАНОВИЧ",
        "bspid": "ESB",
        "city": "НОВОСИБИРСК",
        "street": "СТУДЕНЧЕСКАЯ УЛ.",
        "house": "60",
        "flat": "0",
        "phone": "9137310075"
        }
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data=json)
    answer = response.json()
    print(answer)
    print(json), print(type(json))

    # assert answer['Status'] == 'Err', 'Статус не Err'

# Проверка работы метода когда Error
def test_07_answerErr():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        { "lastname":"МАНАЕНКОВ",
          "name": "ВАСИЛИЙ",
          "midlname": "ИВАНОВИЧ",
          "bspid":"ESB",
          "city": "НОВОСИБИРСК",
          "street": "СТУДЕНЧЕСКАЯ УЛ.",
          "house": "606",
          "flat": "0",
          "phone": "9137310075"
        }
    )
    answer = response.json()

    assert answer['Status'] == 'Err', 'Статус не Err'

def test_08_answerErr():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
        { "lastname":"МАНАЕНКОВ",
          "name": "ВАСИЛИЙ",
          "midlname": "ИВАНОВИЧ",
          "bspid":"ESB",
          "city": "НОВОСИБИРСК",
          "street": "СТУДЕНЧЕСКАЯ УЛ.",
          "house": "606",
          "flat": "0",
          "phone": "9137310075"
        }
    )
    answer = response.json()

    assert answer['Status'] == 'Err', 'Статус не Err'

def test_11_answerErr():
    data = {"lastname": "МАНАЕНКОВ",
            "name": "ВАСИЛИЙ",
            "midlname": "ПЕТРОВИЧ",
            "bspid": "ESB",
            "city": "НОВОСИБИРСК",
            "street": "СТУДЕНЧЕСКАЯ УЛ.",
            "house": "60",
            "flat": "0",
            "phone": "9137310075"
            }
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data=data)
    answer = response.json()
    print(answer)
    # assert answer['Status'] == 'Err', 'Статус не Err'

def test_11_answerNo():
    url='http://10.1.2.83/api/service/FindFnumPersonInform'
    data ={"lastname": "КРАСНОВА", "name": "ВАЛЕНТИНА", "midlname": "ПАВЛОВНА", "bspid": "ESB", "city": "НОВОСИБИРСК",
     "street": "СТУДЕНЧЕСКАЯ УЛ.", "house": "64", "flat": "0", "phone": "9039027487"}
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data=data.encode('utf-8'))
    answer = response.json()
    print(answer)
    # assert answer['Status'] == 'no', 'Статус не Err'

def test12():
    headers = {'Content-type': 'application/json; charset=utf-8'}
    data = {"lastname":"ХОДЫРЕВА",
    "name": "НИНА",
    "midlname": "АЛЕКСАНДРОВНА",
    "bspid":"ESB",
    "city": "НОВОСИБИРСК ",
    "street": "ЧЕРНЯХОВСКОГО УЛ. ",
    "house": "2",
    "flat": "24" ,
    "phone":"9139193389"
    }
    url = f'http://{server}/api/service/FindFnumPersonInform'
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'),  data=data)
    answer = response.json()
    print(answer)
