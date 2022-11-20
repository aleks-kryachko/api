import requests
from conftest import access_token
import time

url = 'https://dev.api.portal.gt.local/api/v1/driver/'
# access_token ='eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJpa2hiNWdhUTJfaWRyQzU0TWktOHdwY0RQNzNET3gxTUpMUXR6TEt6dXZFIn0.eyJleHAiOjE2MjgzMzE3NTAsImlhdCI6MTYyODI0NTM1MCwianRpIjoiMDY4NGVhOWYtN2FkMS00NDI2LWI0MzAtNTg2ZTUxYTgxZmYyIiwiaXNzIjoiaHR0cHM6Ly9kZXYucG9ydGFsLmdsb2JhbHRydWNrLnJ1L2F1dGgvcmVhbG1zL2dsb2JhbHRydWNrIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjczOThjYzRlLTdkZjUtNDJhMy1hY2IxLTIzN2RiY2FmOGZjYyIsInR5cCI6IkJlYXJlciIsImF6cCI6Imd0LWFybSIsIm5vbmNlIjoiZDQxZTY0OTMtMGFmYi00MmIyLTkxMTQtZWU4NzIxODQxNTcyIiwic2Vzc2lvbl9zdGF0ZSI6IjZjMTBjNjRjLTk1MGQtNDU3Zi1iNmFiLTAxMzNlZGUyZDI1MyIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiQ1JNX0NsaWVudE1hbmFnZXIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiU1JNX01hbmFnZXJFeHBlZGl0ZSIsIlNPUF9DbGllbnRNYW5hZ2VyIiwiU1JNX01hbmFnZXJBdHRyYWN0Il19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibW9iaWxlIjo3OTYxNzY1MTQ1MiwibmFtZSI6ItCT0LDQu9C40LDQutCx0LDRgNC-0LLQsCDQndCw0YLQsNC70YzRjyDQk9Cw0LvQuNCw0LrQsdCw0YDQvtCy0LAiLCJncm91cHMiOltdLCJtaWRkbGVOYW1lIjoi0JPQsNC50LHQsNC00YPQu9C70L7QstC90LAiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJnYWxpYWtiYXJvdmFfbmciLCJnaXZlbl9uYW1lIjoi0JPQsNC70LjQsNC60LHQsNGA0L7QstCwINCd0LDRgtCw0LvRjNGPIiwiZmFtaWx5X25hbWUiOiLQk9Cw0LvQuNCw0LrQsdCw0YDQvtCy0LAiLCJlbWFpbCI6Im5hdGFseWEuZ2FsaWFrYmFyb3ZhQGd0bC1oLmNvbSJ9.eUefSv1eum-qLT5NEtx5OW68jcZl9CoiJl7DMA7OKlM0l9wEEF22yV6pw8dIivxvAsWF8RJTu4BNV9BYCszTc3Iz5R-HRb2MIzVdyv0a_9pAINqojLLKjAEHIOOy_0lMlZs8hPYqgG5GXv3Qlmlrs7DM_5GQjmA6dDvlASH7jfBfvBGQbcZd-iConPvE78Ml3dIe166nyHAGdgSxT-I2fF4ll06l3p9y35yIGedoz2d_2_XLP4Y5nsMZxNlowsy0G8X2T_b1Pp_7jp1eEhaEhxtgKQg9iJyWu4cEtjGTUiRf-GGZe6OCgWa4wruSFl5FAaV_btlwvwUPWHYFQ2Ju7w'

"""
access_token берем из браузера импенсолизируемся под Галиакбаровой в файле Current в headeres request Headers authorization: Bearer....
"""

data = {"id": "",
        "lastName": "Булочкин",
        "firstName": "БУБЛИК",
        "patronymic": "ПЕЧЕНЬКИН",
        "phone": +79139130013,
        "sanitation": True,  "robe": True,
        "ownCounterpartyId": "8152721c-090e-44e6-8bda-0116a14bcfdb",
        "birthDate": "2021-06-25T04:08:21.546Z",
        "statusId": "-2",  "statusDate": "2021-06-25T04:08:21.546Z",
        "fullName": "string",  "inn": "123456789012"
}

headers = {'Authorization': f'Bearer {access_token}'}
response =requests.post(url=url, json=data, headers=headers, verify=False)


print(response.json())
# print(response.status_code)

assert (response.status_code) == 200, 'статус не 200'
assert (response.json()['isSuccess']) == True, 'водитель не создан'
assert (response.json()['userMessage']) == 'Регистрация водителя прошла успешна', 'текст не соответствует шаблону'
# assert (response.json()['consName']) == 'gk_cons_dev_wp01'
# assert (response.status_code) != 401, 'нет авторизации нужно изменить токен авторизации'


dataObject = (response.json()['dataObject'])

print("OK, водитель создан")


time.sleep(1)


url = f'https://dev.api.portal.gt.local/api/v1/driver/?id={dataObject}'
headers = {'Authorization': f'Bearer {access_token}'}
response =requests.delete(url=url,  headers=headers, verify=False)
print(url)
print(response.json())
print("OK, водитель удален")
