# -*- coding: utf-8 -*-
"""
Проверка метода sirena/bpmservice/FindAddress
поиск ЛС, Договоров,продукции по адресу.

http://jira.sibirenergo.ru/browse/SRN-1541
http://jira.sibirenergo.ru/browse/SRN-1427

"""
import requests
import json
from conftest import server_ESOR,server_ESTA,server_ESBS,server_ESTO, bspids,server

# json = {"data": {
#         "postal_code": "630090",
#         "country": "Россия",
#         "country_iso_code": "RU",
#         "federal_district": "Сибирский",
#         "region_fias_id": "1ac46b49-3209-4814-b7bf-a509ea1aecd9",
#         "region_kladr_id": "5400000000000",
#         "region_iso_code": "RU-NVS",
#         "region_with_type": "Новосибирская обл",
#         "region_type": "обл",
#         "region_type_full": "область",
#         "region": "Новосибирская",
#         "area_fias_id": '',
#         "area_kladr_id": '',
#         "area_with_type": '',
#         "area_type": '',
#         "area_type_full": '',
#         "area": '',
#         "city_fias_id": "8dea00e3-9aab-4d8e-887c-ef2aaa546456",
#         "city_kladr_id": "5400000100000",
#         "city_with_type": "г Новосибирск",
#         "city_type": "г",
#         "city_type_full": "город",
#         "city": "Новосибирск",
#         "city_area": '',
#         "city_district_fias_id": '',
#         "city_district_kladr_id": '',
#         "city_district_with_type": "Советский р-н",
#         "city_district_type": "р-н",
#         "city_district_type_full": "район",
#         "city_district": "Советский",
#         "settlement_fias_id": '',
#         "settlement_kladr_id": '',
#         "settlement_with_type": '',
#         "settlement_type": '',
#         "settlement_type_full": '',
#         "settlement": '',
#         "street_fias_id": "d5ba7e8e-151b-4ff2-bef8-432921dc9d49",
#         "street_kladr_id": "54000001000135600",
#         "street_with_type": "ул Терешковой",
#         "street_type": "ул",
#         "street_type_full": "улица",
#         "street": "Терешковой",
#         "house_fias_id": "1ff82dfd-e550-4a07-8d2b-514135ee36eb",
#         "house_kladr_id": "5400000100013560012",
#         "house_type": "д",
#         "house_type_full": "дом",
#         "house": "8",
#         "block_type": '',
#         "block_type_full": '',
#         "block": '',
#         "flat_type": "кв",
#         "flat_type_full": "квартира",
#         "flat": "215",
#         "flat_area": '',
#         "square_meter_price": "100387",
#         "flat_price": '',
#         "postal_box": '',
#         "fias_id": "1ff82dfd-e550-4a07-8d2b-514135ee36eb",
#         "fias_code": "54000001000000013560012",
#         "fias_level": "8",
#         "fias_actuality_state": "0",
#         "kladr_id": "5400000100013560012",
#         "geoname_id": '',
#         "capital_marker": "2",
#         "okato": "50401384000",
#         "oktmo": "50701000001",
#         "tax_office": "5473",
#         "tax_office_legal": "5473",
#         "timezone": "UTC+7",
#         "geo_lat": "54.8411358",
#         "geo_lon": "83.0999377",
#         "beltway_hit": '',
#         "beltway_distance": '',
#         "metro": '',
#         "qc_geo": "0",
#         "qc_complete": '',
#         "qc_house": '',
#         "history_values": '',
#         "unparsed_parts": '',
#         "source": '',
#         "qc": ''
#       }}
import pytest
import requests
import datetime
from datetime import date
from conftest import server_ESOR,server_ESTA,server_ESBS,server_ESTO, server_test, server_test_ESBC,server_test_ESOR
from conftest import server_test_ESTO, server_test_ESBI, server_test_ESBY, server_test_ESBB, server_test_ESCH
from conftest import server_test_ESTA
import json
# server_test = '10.1.2.83/sirena'
# url = f'http://{server_test}/bpmservice/FindAddress'
url = 'http://10.1.2.83/sirena/bpmservice/FindAddress'
# Ищем по адресу ЛС, Договор, услугу и тд ESB
def test_01_status_200():
    data = '{"data": {"city": "Новосибирск","street": "Фрунзе","house": "232","flat": "24"}}'

    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data=data.encode('utf-8'))
    answer = response.json()
    print(response.status_code)

    assert response.status_code == 200, 'Сервер не отвечает'

def test_02_ESB():

    data = '{"data": {"city": "Новосибирск","street": "Фрунзе","house": "232","flat": "48"}}'

    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data = data.encode('utf-8'))
    answer = response.json()
    print(answer)

    assert answer['data'][0]['Values'][0]['ID'] == '1664720', 'Номер договора не тот '
    assert answer['data'][0]['Values'][0]['AddressID'] == '520971'
    assert answer['data'][0]['Values'][0]['FaceNum'] == '10370148', 'Лицевой счет не тот'
    assert answer['data'][0]['Values'][0]['NDogovor'] == '1664720', 'Номер договора не тот '
    assert answer['data'][0]['Values'][0]['TypeDgText'] == 'Э/Энергия', 'Не та услуга'
    assert answer['data'][0]['Values'][0]['AccountID'] == '3137690'
    assert answer['data'][0]['Values'][1]['NDogovor'] == '1966218', 'Не тот договор на Доп услугу'
    assert answer['data'][0]['Values'][1]['TypeDgText'] == 'Дополнительные услуги Новосибиркэнергосбыт'

def test_03_ESTO():

    data = '{"data": {"city":"ТОГУЧИН","street":"ЛЕНИНА","house":"4/3","flat":"14"}}'

    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data = data.encode('utf-8'))
    answer = response.json()
    print(response.status_code, answer)

    assert answer['data'][0]['Values'][0]['ID'] == '55778'
    assert answer['data'][0]['Values'][0]['AddressID'] == '42680'
    assert answer['data'][0]['Values'][0]['FaceNum'] == '404314'
    assert answer['data'][0]['Values'][0]['NDogovor'] == '55778'
    assert answer['data'][0]['Values'][0]['TypeDgText'] == 'Э/Энергия'
    assert answer['data'][0]['Values'][0]['AccountID'] == '93383'

def test_04_ESOR():
    url = f'http://{server}/sirena/bpmservice/FindAddress'
    data = '{"data": {"city":"Ордынское","street":"ЛЕНИНА","house":"7","flat":"11"}}'

    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data=data.encode('utf-8'))
    answer = response.json()
    print(response.status_code, answer)

    assert answer['data'][0]['Values'][0]['ID'] == '19257'
    assert answer['data'][0]['Values'][0]['AddressID'] == '307000000000012156'
    assert answer['data'][0]['Values'][0]['FaceNum'] == '5005032'
    assert answer['data'][0]['Values'][0]['NDogovor'] == '19257'
    assert answer['data'][0]['Values'][0]['TypeDgText'] == 'Дополнительные услуги Новосибиркэнергосбыт'
    assert answer['data'][0]['Values'][1]['TypeDgText'] == 'Общедомовые нужды (э/э)'
    assert answer['data'][0]['Values'][2]['TypeDgText'] == 'Э/Энергия'

def test_05_ESBC():
    url = f'http://{server}/sirena/bpmservice/FindAddress'
    data = '{"data": {"city":"ЧУЛЫМ","street":"ЛЕНИНА","house":"2","flat":"10"}}'

    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data = data.encode('utf-8'))
    answer = response.json()
    print(response.status_code, answer)

    assert answer['data'][0]['Values'][0]['ID'] == '17594'
    assert answer['data'][0]['Values'][0]['AddressID'] == '101000000000003870'
    assert answer['data'][0]['Values'][0]['FaceNum'] == '200210'
    assert answer['data'][0]['Values'][0]['NDogovor'] == '17594'
    assert answer['data'][0]['Values'][0]['TypeDgText'] == 'Общедомовые нужды (э/э)'
    assert answer['data'][0]['Values'][1]['NDogovor'] == '18742'
    assert answer['data'][0]['Values'][2]['NDogovor'] == '33558'
