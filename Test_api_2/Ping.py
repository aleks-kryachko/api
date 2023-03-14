from ping3 import ping
import requests
url = 'google.com'
r = requests.get('http://google.com')
print(url, r.status_code)
otvet = ping(url, timeout=20, ttl=20)
print(otvet)
