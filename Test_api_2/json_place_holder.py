import  requests
import json
# https://realpython.com/testing-third-party-apis-with-mocks/
# https://opensource.com/article/21/9/unit-test-python

url = 'http://jsonplaceholder.typicode.com/todos'
r = requests.get(url=url)
# assert r.status_code == 200, 'Ответа нет'
answer = r.json()
answer_json = answer[0]
if r.status_code != 200:
    print('статус не 200')
# if заменить на asert
print(answer_json)

