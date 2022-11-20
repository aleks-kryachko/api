# -*- coding: utf-8 -*-
# Перевозчик ООО "7 АРТ М"

import random
import requests
import pytest
from conftest import token, url, env

headers = {'Authorization': 'Bearer ' + token}
url ='https://preprod.api.portal.globaltruck.ru/api/v1'


response = requests.get(url=url,  headers=headers, verify=False)

def test_01_check_status_response():

  print(response.text)
  assert response.status_code == 200, 'Статус не 200'
