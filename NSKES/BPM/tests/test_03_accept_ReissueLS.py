"""
Переоформление ЛС на другово собственика (например при купли-продаже)
http://jira.sibirenergo.ru/browse/SRN-1281
http://jira.sibirenergo.ru/browse/SRN-1570

IdDogovor - номер договора
IdAddress - из теста test_FindAdress

Выходным параметром является json, в формате
{"Error":"1","Message":"Договора не существует"}
{"Error":"1","Message":"Договор не создался. Такой лицевой уже есть"}
"""
import requests
import json
from conftest import server_ESOR,server_ESTA,server_ESBS,server_ESTO, bspids,server

url = f'http://{server}/bpmservice/ReissueLS'
#url = 'http://10.1.14.31/rest/ReissueLS'
#url = 'http://10.1.14.31/sirena/bpmservice/ReissueLS'


def test_01_status_200():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
    {
        "Family": "Жуков", "Name": "Георгий", "Otch": "Константинович", "DoB": "2/11/1980",
        "PoB": "Стрелковка", "Series": "1111", "Number": "222222", "PassDate": "3/11/2000", "DateEGRN": "23/08/2020",
        "HCount": 3, "Sobst": "1", "IdDogovor": 12, "IdAddress": "101000000000019959"
    }
                             )
    assert response.status_code == 200, 'Сервер не отвечает'

def test_03_ESB_adress_different():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
    {
        "Family": "Жуков", "Name": "Георгий", "Otch": "Константинович", "DoB": "2/11/1980",
         "PoB": "Стрелковка", "Series": "1111", "Number": "222222", "PassDate": "3/11/2000", "DateEGRN": "23/08/2020",
        "HCount": 3, "Sobst": "1", "IdDogovor": 15, "AddressID": "520948", "BSPID": "ESB"
    }
                             )
    answer = response.json()
    assert answer['Error'] == '1'
    assert answer['Message'] == 'Адрес отличается от указанного в договоре'
    print(answer)

def test_03_ESB_dogovor_not_exist():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
    {
        "Family": "Жуков", "Name": "Георгий", "Otch": "Константинович", "DoB": "2/11/1980",
        "PoB": "Стрелковка", "Series": "1111", "Number": "222222", "PassDate": "3/11/2000", "DateEGRN": "23/08/2020",
        "HCount": 3, "Sobst": "1", "IdAddress": "101000000000019959", "BSPID": "ESB"
    }
                             )
    answer = response.json()
    assert answer['Error'] == '1'
    assert answer['Message'] == 'Договора не существует'
    print(answer)

def test_03_ESB():
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json=
    {
         "Family": "ДАЩЕНКО", "Name": "ЕГОР", "Otch": "СЕРГЕЕВИЧ", "DoB": "2/11/1980",
         "PoB": "Стрелковка", "Series": "1111", "Number": "222222", "PassDate": "3/11/2000", "DateEGRN": "23/08/2019",
         "HCount": 3, "Sobst": "1", "IdDogovor": '1664697', "IdAddress": "520948", "BSPID": "ESB"
    }
                             )
    answer = response.json()
    assert answer['Error'] == '1'
    assert answer['Message'] == 'Договор не создался. Такой лицевой уже есть'
    print(answer)

def test_04_ESB_reneval_LS():
    """
    Перед переформление необходимо передать показания, Руками через сирену ЛС=> Сверка=> расчет
    на дату за день или две на дату DateEGRN

    """

    #  Узнаем из FindAddress Номер Договора , номер ЛС , и AddressID
    # data = '{"data": {"city": "Новосибирск","street": "Фрунзе","house": "232","flat": "30"}}'
    data = '{"data": {"city": "Новосибирск","street": "Фрунзе","house": "232","flat": "42"}}'
    url = f'http://{server}/sirena/bpmservice/FindAddress'
    response = requests.post(url=url, auth=('bpm', 'bpmbpm'), data=data.encode('utf-8'))
    answer = response.json()
    accaunt_nimber = answer['data'][0]['Values'][0]['FaceNum']
    contract_number = answer['data'][0]['Values'][0]['NDogovor']
    addressid_number = str(answer['data'][0]['Values'][0]['AddressID'])
    print('\n',
          '№ ЛС      ', accaunt_nimber, '\n'
          ' № договора', contract_number, '\n'          
          ' AddressID ', addressid_number, '\n')


    # Попытаемся переоформить ЛС на другое имя мспользуя номер договора и AddressID

    data_reneval = f'{{"Family":"Тест","Name":"Тест","Otch":"СЕРГЕЕВИЧ","DoB":"2/11/1980",' \
                   f'"PoB":"Стрелковка","Series":"1111","Number":"222222","PassDate":"3/11/2000", "PassIssuedBy": "ОВД какого-то района", ' \
                   f'"DateEGRN": "16/09/2020","HCount":3,"Sobst":"1","IdDogovor":{contract_number},' \
                   f'"IdAddress":"{addressid_number}","BSPID":"ESB","NewAbonentEmail":"kor@mail.ru","NewAbonentPhone":"9139062856"}}'

    url_reneval = f'http://{server}/sirena/bpmservice/ReissueLS'
    response_reneval = requests.post(url=url_reneval, auth=('bpm', 'bpm1'), data=data_reneval.encode('utf-8'))
    answer = response_reneval.json()
    print(answer, '\n')

    assert answer[0] == '0', 'ошибка при переоформлении'
    assert answer[1] == 'Лицевой счёт успешно переоформлен', 'ошибка при переоформлении'







