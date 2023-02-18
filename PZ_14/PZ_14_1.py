# В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным).

import re  # Импортируем регулярное выражение

with open('radio_stations.txt', 'r') as file:
    radio_list = re.findall(r"(?<=//)(?P<domen>[\w.\-\d:]+)", file.read())  # Открываем файл и сразу ищем домены

print(radio_list)  # Выводим домены
