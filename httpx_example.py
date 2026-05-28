import httpx

## Основные функции HTTPX
# Отправка GET-запроса
response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())

# Отправка POST-запроса
data = {
    'userId': 1,
    'title': 'New tasks',
    'completed': False
}
response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
print(response.status_code)
# print(response.request.headers)
print(response.json())

# Отправка данных в application/x-www-form-urlencoded
data = {"username": "test_user", "password": "123456"}
response = httpx.post('https://httpbin.org/post', data=data)
print(response.status_code)
# print(response.request.headers)
print(response.json())

# Передача заголовков
headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get('https://httpbin.org/get', headers=headers)
print(response.request.headers)
print(response.json())

# Работа с параметрами запроса
params = {'userId': 1}
response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
print(response.url)
print(response.json())

# Отправка файлов
file = {'file': ('example.txt', open('example.txt', 'rb'))}
response = httpx.post('https://httpbin.org/post', files=file)
print(response.json())

## Работа с сессиями
# Использование httpx.Client
with httpx.Client() as client:
    response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
print(response1.json())
print(response2.json())

# Добавление базовых заголовков в Client
client = httpx.Client(headers={'Authorization': 'Bearer my_secret_token'})
response = client.get('https://httpbin.org/get')
print(response.json())

## Работа с ошибками
# Проверка статуса ответа (raise_for_status)
try:
    response = httpx.get('https://jsonplaceholder.typicode.com/invalid_url')
    print(response.status_code)
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'Ошибка запроса: {e}')

# Обработка таймаутов
try:
    response = httpx.get('https://httpbin.org/delay/5', timeout=2)
except httpx.ReadTimeout:
    print('Запрос превысил лимит времени')
