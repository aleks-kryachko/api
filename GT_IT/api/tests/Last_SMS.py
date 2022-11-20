# -*- coding: utf-8 -*-
import requests
from jsonschema import Draft7Validator
import json
import pytest
# url = "https://staging.api.portal.gt.local/api/v1/lastsms/1"
# # url = "https://dev.api.portal.gt.local/api/v1/lastsms/1"
from conftest import token, url, env
headers = {'Authorization': 'Bearer ' + token}

response = requests.get(url=url,  headers=headers, verify=False)
response_json = response.json()
assert response.status_code == 200, 'Статус не 200'
print(response.json())
def test_01_check_status_response():

    assert response.status_code == 200, f'Статус не 200 статус '


# валидируем JSON по схеме
def test_02_check_schemas():
    schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "numericPhoneNumber": {"type": "number"},
            "sentTime": {"type": "string"},
            "smsToken": {"type": "number" or 'null'},
            "smsText": {"type": "string" or 'null'},
                }
            }}
    # response_json = json.loads(json_data)
#указываем в каком именно месте не соответствует JSON
    v = Draft7Validator(schema)
    errors = sorted(v.iter_errors(response_json), key=lambda e: e.path)
    msg = """"""
    for error in errors:
        msg += str(error.message)
        msg += """\r\n"""
        for suberror in sorted(error.context, key=lambda e: e.schema_path):
            msg += str(suberror.message)
            msg += """\r\n"""

    assert Draft7Validator(schema).is_valid(response_json), f"Ошибка Валидации: {msg} "

    print(response.json())
    print(env)
    print({response.status_code})
