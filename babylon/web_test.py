import asyncio
import websockets

async def test_websocket():
    uri = "ws://127.0.0.1:8000/ws/chat/sala_de_guerra/"
    try:
        async with websockets.connect(uri) as websocket:
            print("Conectado ao WebSocket!")
            await websocket.send('{"message": "Olá", "username": "Tester"}')
            response = await websocket.recv()
            print(f"Recebido: {response}")
    except Exception as e:
        print(f"Erro ao conectar: {e}")

asyncio.run(test_websocket())
