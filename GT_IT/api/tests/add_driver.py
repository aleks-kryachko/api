# -*- coding: utf-8 -*-
# Перевозчик ООО "7 АРТ М"
# https://staging.portal.globaltruck.ru/srm/orgs/c033a437-fe5c-4310-a0c8-54eb43238400/

import random
import requests
import pytest
from conftest import token, url,env
x = "QWERTYUIOPASDFGHJKLZXCVBNM"
y = "qwertyuiopasdfghjklzxcvbnm"
wnCounterpartyId= 'c033a437-fe5c-4310-a0c8-54eb43238400'
headers = {'Authorization': 'Bearer ' + token}
data = {
  "id": "",
  "lastName": f'{(random.choice(x)+random.choice(y)+random.choice(y)+random.choice(y)+random.choice(y)+random.choice(y))}',
  "firstName": f'{(random.choice(x)+random.choice(y)+random.choice(y)+random.choice(y)+random.choice(y)+random.choice(y))}',
  "patronymic": f'{(random.choice(x)+random.choice(y)+random.choice(y)+random.choice(y)+random.choice(y)+random.choice(y))}',
  "phone": +79139141516,
  "sanitation": True,
  "robe": True,
  "ownCounterpartyId": "c033a437-fe5c-4310-a0c8-54eb43238400",
  "birthDate": "2021-06-25T04:08:21.546Z",
  "statusId": "3",
  "statusDate": "2021-06-25T04:08:21.546Z",
  "fullName": "string",
  "inn": "123456789012"
}
if env == 'preprod':
  url ='https://preprod.api.portal.globaltruck.ru/api/v1/driver'


response = requests.post(url=url,  headers=headers, verify=False, json=data)

def test_01_check_status_response():

  print(response.json())
  assert response.status_code == 200, 'Статус не 200'
# валидируем JSON по схеме успех
def test_02_check_status_Success():
  assert response.json()['isSuccess'] == True, 'Статус не успех'


def test_03_check_text_Message():
  assert response.json()['userMessage'] == 'Регистрация водителя прошла успешна', 'сообщение не соответствует'

# resultId = response.json()['resultId']
# dataObject = response.json()['dataObject']
# print(resultId)
# def test_04_should_be_delete_driver():
#   url = f'https://staging.api.portal.gt.local/api/v1/driver{resultId}'
#   response_del = requests.delete(url=url, headers=headers, verify=False)
#   print(response_del.json())
  # assert response_del.json()['isSuccess'] == True, 'сообщение не соответствует'
  # assert response_del.json()['userMessage'] == 'Водитель успешно удалён', 'сообщение не соответствует'

# def test_04_should_be_vehicle():
#   # ID = 'c033a437-fe5c-4310-a0c8-54eb43238400'
#   url = 'https://dev.api.portal.gt.local/api/v1/vehicle?counterpartyId=vtcyiclec033a437-fe5c-4310-a0c8-54eb43238400'
#   response = requests.get(url=url, headers=headers, verify=False)
#   # https://staging.api.portal.gt.local/api/v1/vehicle?counterpartyId=c033a437-fe5c-4310-a0c8-54eb43238400
#   print(response)
print(response.json())
print(env)
print({response.status_code})
