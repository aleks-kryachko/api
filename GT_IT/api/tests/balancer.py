import requests
from conftest import access_token

url='https://dev.api.portal.gt.local/api/v1'
headers = {'Authorization': f'Bearer {access_token}'}
session = requests.Session()
r = session.get(url=url, headers=headers, verify=False)
print(r.text)
print(r.status_code)
assert (r.status_code) == 200, 'статус не 200'

