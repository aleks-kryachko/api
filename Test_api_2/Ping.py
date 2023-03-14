# https://ru.stackoverflow.com/questions/1442249/timeout-ping3-%D1%81%D1%80%D0%B0%D0%B7%D1%83-%D0%BE%D1%82%D0%B4%D0%B0%D0%B5%D1%82-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-false
# https://www.delftstack.com/howto/python/python-ping/
from ping3 import ping
import requests
import time
while True:
    # Code executed here
    time.sleep(2)

    url = 'google.com'
    Status = 0
    r = requests.get('http://google.com')
    # print(url, r.status_code)
    assert r.status_code == 200, 'Заданный узел недоступен'
    otvet = ping(url, timeout=20, ttl=20)
    print(otvet)
    if otvet in (None, False):
                    print('Offline: ')
                    Status = 'Offline'
    else:
                    print('Online: ')
                    Status = 'Online'
    # return Status

    from pythonping import ping

    ping('google.com', verbose=True)
