import asyncio
import websockets
from websockets import ServerConnection


async def echo_websocket(websocket: ServerConnection):
    async for message in websocket:
        print(f'Получено сообщение: {message}')

        for _ in range(5):
            await websocket.send(f'Сообщение пользователя: {message}')


async def main_websocket():
    server = await websockets.serve(echo_websocket, 'localhost', 8765)
    print('Websocket сервер запущен на ws://localhost:8765')

    await server.wait_closed()


asyncio.run(main_websocket())
