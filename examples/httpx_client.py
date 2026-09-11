import httpx


# Проходим аутентификацию
login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'Login data:', login_response_data)

# Инициализируем клиент c авторизацией, с base_url и timeout
client = httpx.Client(
    base_url='http://localhost:8000',
    timeout=10,  # Таймаут в секундах
    headers={"Authorization": f'Bearer {login_response_data['token']['accessToken']}'}
)

# Выполняем GET-запрос с авторизацией, используя относительный путь
get_user_me_response = client.get('/api/v1/users/me')
get_user_me_response_data = get_user_me_response.json()

# Выводим ответ в консоль
print(f'Get user me data:', get_user_me_response_data)
