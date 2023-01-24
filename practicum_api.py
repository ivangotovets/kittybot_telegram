import requests

from pprint import pprint

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': 'OAuth y0_AgAAAAAq07KhAAYckQAAAADan1QAHASybtahRn-xqAnibil4xyrVrp8'}
payload = {'from_date': 1549962000}

# Делаем GET-запрос к эндпоинту url с заголовком headers и параметрами params
homework_statuses = requests.get(url, headers=headers, params=payload)

# Печатаем ответ API в формате JSON
# print(homework_statuses.text)

# А можно ответ в формате JSON привести к типам данных Python и напечатать и его
pprint(homework_statuses.json())