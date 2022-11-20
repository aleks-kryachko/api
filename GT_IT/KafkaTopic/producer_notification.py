# bootstrap-servers: rc1b-c7mo8si0i96vdqrb.mdb.yandexcloud.net:9091
# username: new-srm-project
# password: GEn2jFVRxhVggLp
# notifications
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='rc1b-c7mo8si0i96vdqrb.mdb.yandexcloud.net:9091',
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_password='GEn2jFVRxhVggLp',
    sasl_plain_username='new-srm-project',
    ssl_cafile="C:/Users/Kryachko_AI/Yandex/YandexCA.crt")

msg = """{"userId":null,"userAdId":null,"data":"111!!!","event":null,"subject":"by","types":["email"],"files":null,"source":"SRM","replyTo":null,"phoneNumber":null,"pushObject":null,"urlPush":null,"email":"plusv@yandex.ru"}"""

producer.send('notifications', msg.encode())
producer.flush()
producer.close()
