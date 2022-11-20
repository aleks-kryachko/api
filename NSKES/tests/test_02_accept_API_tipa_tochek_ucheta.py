"""
задача SRN-1262

Тестирование API - выдачу полей в Json для Точек Учета
Сирена подготавливает данные для BPM

Автотест задачи SRN-1262 .
1 тест Проверяем статус 200 (вообще есть ли Json)
2 тест Проверяем тип, название(уникальность) полей вывода в Json
Проверяем договора с ТУ(точкой учета), без ТУ, ТУ с ПУ(прибор учета), с 2 ПУ, с 3 ПУ, без ПУ и т.д.

730162, 73016 ТУ с 1 тарифным  - данные по 1 ПУ
229623  c 2x тарифным          - данные по двум ПУ
1811074, 793815  с 3х тарифным - данные по трем ПУ
2076016 без точки учета        - данных нет, возвращает []
1699259 вообще "левая цифра"   - данных нет, возвращает []
1                              - с деактивированной точкой учета
398777                         - у ПУ нет данных
19817                          - договор расторгнут

TODO:
    * улучшение. Добавить проверку возможных двух типов данных 'string' или 'null'
    * улучшение. Добавить проверку у 2х тарифных ПУ, проверку второго тарифа
"""
import pytest
import requests
import json
from jsonschema import Draft4Validator

session = requests.Session()
headers = {'login_username': 'bpm',
           'login_password': 'bpm1'}

responses = []
datas = []
for unic_url in ["730162", "73016", '229623', '1811074', '793815', '2076016', '1699259', '1', '398777', '19817']:
    url = f'http://10.1.2.31:57772/sirena/bpmservice/getTUList?contractId=sirena\\Contracts.EPhDogovor\\ESB\\{unic_url}'
    response = session.get(url=url, auth=(headers['login_username'], headers['login_password']))
    responses.append(response)
    datas.append(response.json())

@pytest.mark.parametrize("response_unic", responses)
def test_01_check_status_response(response_unic):
    """
    Проверка Http статус успешности ответа сервера (200)
    :param response_unic: ответ сервера
    :return:
    """
    assert response_unic.status_code == 200, 'Статус не 200'

@pytest.mark.parametrize("response_unic", responses)
def test_02_check_schemas(response_unic):

    json_data = response_unic.json()
    schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "CalculatedReading": {"type": "string"},
                    "CalculationMethod": {"type": "string"},
                    'ContractId': {"type": "string"},
                    'CounterType': {"type": "string"},
                    #'Description': {"type": "string" and 'null'},   #не активная т.к возможно три типа вывода данных (null, строка, число)
                    'Digit': {"type": "string"},
                    'EndStateChkDate': {"type": "string"},
                    'Item': {"type": "number"},
                    'LastReadingDate': {"type": "string"},
                    'Location': {"type": "string"},
                    'MPI': {"type": "number"},
                    'NumTu': {"type": "string"},
                   # 'Phase': {"type": "number" or 'null'},
                    'ReadingMeter': {"type": "string"},
                    'RegPointId': {"type": "string"},
                    'SerialNum': {"type": "string"},
                    'StatusCode': {"type": "number"},
                    'Summ': {"type": "number"},
                    'Taxa': {"type": "number"},
                    #'ValueType': {"type": "string" or 'null'}
                },
                "required": ["CalculatedReading", "CalculationMethod", 'ContractId', 'CounterType', 'Description',
                             'Digit', 'Digit', 'EndStateChkDate', 'Item', 'LastReadingDate', 'Location',
                             'MPI', 'NumTu', 'Phase', 'ReadingMeter', 'RegPointId', 'SerialNum', 'StatusCode',
                             'Summ', 'Taxa', 'ValueType']
            }
    }
    assert Draft4Validator(schema).is_valid(json_data), "Ошибка Валидации"