import socket

user_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_client_socket.connect(('localhost', 12345))

user_client_socket.send('Привет, сервер!'.encode())
print(user_client_socket.recv(1024).decode())

user_client_socket.close()
