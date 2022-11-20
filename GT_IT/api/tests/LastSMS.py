import requests
from conftest import access_token, env

url = f' https://{environment}.api.portal.gt.local/api/v1/lastsms/1'

headers = {'Authorization': f'Bearer {access_token}'}
session = requests.Session()
r = session.get(url=url, headers=headers, verify=False)
# assert (r.status_code) == 200, 'статус не 200'
print(r.text)
print(env)

