import httpx

# Работа с эндпоинтом /api/v1/authentication/login
login_payload = {
    'email': 'user@example.com',
    'password': 'string'
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print('Login response:', login_response_data)
print('Status Code:', login_response.status_code)

get_user_headers = {'Authorization': f'Bearer {login_response_data['token']['accessToken']}'}

get_user_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=get_user_headers)
get_user_response_data = get_user_response.json()
print('Get user response:', get_user_response_data)
print('Get user status code:', get_user_response.status_code)

refresh_payload = {
    'refreshToken': login_response_data['token']['refreshToken']
}
refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()
print('Refresh response:', refresh_response_data)
print('Status Code:', refresh_response.status_code)
