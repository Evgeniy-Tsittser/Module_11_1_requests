import requests

# Выполнение GET-запроса для получения информации о пользователе
response = requests.get('https://api.github.com/users/Evgeniy-Tsittser')

# Проверяем статус ответа
if response.status_code == 200:
    data = response.json()
    print("GET-запрос успешен. Информация о пользователе:")
    print(data)
else:
    print(f"Ошибка выполнения GET-запроса. Статус код: {response.status_code}")

# Выполнение POST-запроса (создание репозитория)
payload = {
    "name": "test-repo-1223",
    "private": False
}
headers = {
    "Authorization": "token с моим токеном запрос работает:)",
    "Accept": "application/vnd.github.v3+json"
}
response = requests.post('https://api.github.com/user/repos', json=payload, headers=headers)

# Проверяем статус ответа
if response.status_code == 201:
    data = response.json()
    print("\nPOST-запрос успешен. Информация о созданном репозитории:")
    print(data)
else:
    print(f"Ошибка выполнения POST-запроса. Статус код: {response.status_code}")

# Выполнение GET-запроса с параметрами (список репозиториев пользователя)
params = {'sort': 'full_name'}
response = requests.get('https://api.github.com/users/Evgeniy-Tsittser/repos', params=params)

# Проверяем статус ответа
if response.status_code == 200:
    data = response.json()
    print("\nGET-запрос с параметрами успешен. Список репозиториев:")
    print(data)
else:
    print(f"Ошибка выполнения GET-запроса с параметрами. Статус код: {response.status_code}")

# GET-запрос с заголовками (информация о репозитории)
headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://api.github.com/repos/Evgeniy-Tsittser/HomeworkMod2_5', headers=headers)

# Проверяем статус ответа
if response.status_code == 200:
    data = response.json()
    print("\nGET-запрос с заголовками успешен. Информация о репозитории:")
    print(data)
else:
    print(f"Ошибка выполнения GET-запроса с заголовками. Статус код: {response.status_code}")