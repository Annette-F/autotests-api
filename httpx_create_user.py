import httpx
from tools.fakers import fake  # Импортируем функцию для генерации случайного email
from faker import Faker

faker = Faker()

# Создание пользователя

payload = {
    'email': fake.email(),,  # Используем функцию для генерации случайного email
    'password': faker.password(),
    'lastName': faker.last_name(),
    'firstName': faker.first_name(),
    'middleName': 'string'
}

response = httpx.post('http://localhost:8000/api/v1/users', json=payload)
print(response.status_code)
print(response.json())
