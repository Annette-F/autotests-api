import socket


def user_server():
    user_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    user_server_socket.bind(('localhost', 12345))
    user_server_socket.listen(10)

    messages: list[str] = []

    while True:
        user_client_socket, user_client_address = user_server_socket.accept()
        print(f'Пользователь с адресом: {user_client_address} подключился к серверу')

        message = user_client_socket.recv(1024).decode()
        print(f'Пользователь с адресом: {user_client_address} отправил сообщение: {message}')
        messages.append(message)

        user_client_socket.send('\n'.join(messages).encode())
        user_client_socket.close()


if __name__ == '__main__':
    user_server()
