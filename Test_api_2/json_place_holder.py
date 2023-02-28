import  requests
import json
import jsonschema
from jsonschema import Draft7Validator
# https://realpython.com/testing-third-party-apis-with-mocks/
# https://opensource.com/article/21/9/unit-test-python

url = 'http://jsonplaceholder.typicode.com/todos'
r = requests.get(url=url)
# assert r.status_code == 200, 'Ответа нет'
answer = r.json()
answer_json = answer[0]

assert(r.status_code == 200), 'статус не 200'

assert answer_json == {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, 'нет информации для вывода'
# url = 'https://jsonplaceholder.typicode.com/posts/1'
# r = requests.get(url=url)

json_data = r.json()
schema = {
"items":{
   "userId": "number",
   "id": "number",
   "title": "string",
    "completed": "False"},
          }
required: ["userId", "id", "title", "completed"]
assert Draft7Validator(schema).is_valid(json_data), "Ошибка Валидации"
print(answer_json)
