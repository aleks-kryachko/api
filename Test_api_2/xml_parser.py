import xml.etree.ElementTree as ET
import requests
import datetime


date_today = datetime.datetime.today().strftime('%Y-%m-%d')


# https://docs.python.org/3/library/xml.etree.elementtree.html
url = 'https://www.washingtonpost.com/arcio/news-sitemap/'
# 'https://www.google.com/schemas/sitemap-news/0.9/sitemap-news.xsd'
r = requests.get(url=url)
# assert r.status_code == 200, 'Ответа нет'
# answer = r.json()
root = ET.fromstring(r.content)
assert(r.status_code == 200), 'статус не 200'
for element in root.iter(tag='news:news'):
    assert element.text == 'Washington Post', 'Нет информации для вывода. Ответ Пуст'
for element in root.iter(tag='news:publication_date'):
    assert element.text =='date_today', 'Дата не соответствует'
print(date_today)
# sql test
# 'https://pypi.org/project/sql-test/'
# https://learn.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server?view=sql-server-ver16
# https://stackoverflow.com/questions/11451101/retrieving-data-from-sql-using-pyodbc