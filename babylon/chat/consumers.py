from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'sala_de_guerra'
        self.room_group_name = f'chat_{self.room_name}'

        try:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            print(f"Conexão WebSocket aceita: {self.channel_name}")
        except Exception as e:
            print(f"Erro ao conectar: {e}")

    async def disconnect(self, close_code):
        try:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
            print(f"Conexão WebSocket fechada: {self.channel_name}")
        except Exception as e:
            print(f"Erro ao desconectar: {e}")

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            username = text_data_json['username']

            print(f"Mensagem recebida: {message} de {username}")

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                }
            )
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")

    async def chat_message(self, event):
        try:
            message = event['message']
            username = event['username']

            print(f"Enviando mensagem para o grupo: {message} de {username}")

            await self.send(text_data=json.dumps({
                'message': message,
                'username': username,
            }))
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")