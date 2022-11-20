# bootstrap-servers: rc1b-c7mo8si0i96vdqrb.mdb.yandexcloud.net:9091
# username: new-srm-project
# password: GEn2jFVRxhVggLp
# notifications

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'notification_test',
    bootstrap_servers='rc1b-c7mo8si0i96vdqrb.mdb.yandexcloud.net:9091',
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_password='GEn2jFVRxhVggLp',
    sasl_plain_username='new-srm-project',
    ssl_cafile="C:/Users/Kryachko_AI/Yandex/YandexCA.crt")

print("ready")

for msg in consumer:
    print(msg.value.decode("utf-8"))
