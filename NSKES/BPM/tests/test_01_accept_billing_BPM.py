# -*- coding: utf-8 -*-
"""
Запрос биллинговых данных из Сирены
1. ESB многоквартирный дом
2. ESB частный дом
3. ESTO частный
4. ESTO многоквартирный
5. ESOR частный
6. ESOR многоквартирный
7. ESBC частный
8. ESBC многоквартирный

пеня будет считаться только с findType : 2
"""
import requests
import json
from conftest import server_ESOR, server_ESTA, server_ESBS, server_ESTO, server_test

server_test = '10.1.2.83/sirena'
url = f'http://{server_test}/bpmservice/GetSirenaContractData'

def test_01_billing_ESB():
        datas = [
                [{"SirenaContractId": "\\Contracts.EPhDogovor\\ESB\\1"}],
                [{"SirenaContractId": "\\Contracts.EPhDogovor\\ESB\\2"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\100012"}]
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000122"}],
                [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\3"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000124"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000125"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000126"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000129"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000133"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000136"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000137"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000138"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\100014"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000140"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000141"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000143"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000144"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000149"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000150"}],
                # [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\1000151"}]
        ]
        for data in datas:
            response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json={"findType": 2,"contracts":data})


            print(response.status_code, response.json())
            answer = response.json()
            answer_json = answer[0]
            assert response.status_code == 200, 'Ответа нет'
            assert answer_json['debtSumm'] != None, 'Нет в ответе значения debtSumm'
            assert answer_json['lastPaymentDate'] != None, 'Нет в ответе значения lastPaymentDate'
            assert answer_json['lastPaymentSum'] != None, 'Нет в ответе значения lastPaymentSum'

def test_02_billing_ESTO():
        datas = [
                [{"SirenaContractId": "\\Contracts.EPhDogovor\\ESTO\\29299"}],
                [{"SirenaContractId": "\\Contracts.EPhDogovor\\ESTO\\55778"}]    # ЛС 404314
        ]
        for data in datas:
                response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json={"findType": 2, "contracts": data})

                print(response.status_code, response.json())
                answer = response.json()
                answer_json = answer[0]
                assert response.status_code == 200, 'Ответа нет'
                assert answer_json['debtSumm'] != None, 'Выходной JSON сломан'
                assert answer_json['lastPaymentDate'] != None, 'Выходной JSON сломан'
                assert answer_json['lastPaymentSum'] != None, 'Выходной JSON сломан'

def test_03_billing_ESOR():
        datas = [
                [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESOR\\101000000000000005"}],
                [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESOR\\101000000000012344"}]
        ]
        for data in datas:
                response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json={"findType": 2, "contracts": data})

                print(response.status_code, response.json())
                answer = response.json()
                answer_json = answer[0]
                assert response.status_code == 200, 'Ответа нет'
                assert answer_json['debtSumm'] != None, 'Выходной JSON сломан'
                assert answer_json['lastPaymentDate'] != None, 'Выходной JSON сломан'
                assert answer_json['lastPaymentSum'] != None, 'Выходной JSON сломан'

def test_03_billing_ESBC():
        datas = [
                [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESBC\\1000"}],
                [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESBC\\7324"}],


        ]
        for data in datas:
                response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json={"findType": 2, "contracts": data})

                print(response.status_code, response.json())
                answer = response.json()
                answer_data = answer[0]
                assert response.status_code == 200, 'Ответа нет'
                assert answer_data['debtSumm'] != None, 'Выходной JSON сломан'
                assert answer_data['lastPaymentDate'] != None, 'Выходной JSON сломан'
                assert answer_data['lastPaymentSum'] != None, 'Выходной JSON сломан'

def test_04_check_moneysbor_ESB():
        data = [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESB\\730162"}]
        findtypes = [0, 1, 2, 3]

        for findtype in findtypes:
                response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json={"findType": findtype,"contracts":data})

                print(response.status_code, response.json())
                answer = response.json()
                answer_json = answer[0]
                assert answer_json['MoneySbor'] == 'РСО (Прямые договора)', 'Нет в ответе MoneySbor'

def test_05_check_moneysbor_ESTO():
        data = [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESTO\\55778"}]  # ЛС 404314
        findtypes = [0, 1, 2, 3]

        for findtype in findtypes:
                response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json={"findType": findtype, "contracts": data})

                print(response.status_code, response.json())
                answer = response.json()
                answer_json = answer[0]
                assert answer_json['MoneySbor'] == '', 'Нет в ответе MoneySbor'

def test_06_check_moneysbor_ESBC():
        data = [{"SirenaContractId": "sirena\\Contracts.EPhDogovor\\ESBC\\7324"}]
        findtypes = [0, 1, 2, 3]

        for findtype in findtypes:
                response = requests.post(url=url, auth=('bpm', 'bpmbpm'), json={"findType": findtype, "contracts": data})

                print(response.status_code, response.json())
                answer = response.json()
                answer_data = answer[0]
                assert answer_data['MoneySbor'] == 'Не определено', 'Нет в ответе MoneySbor'

