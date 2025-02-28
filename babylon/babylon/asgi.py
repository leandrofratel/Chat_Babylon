import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # Importando corretamente o routing do chat

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'babylon.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Gerencia requisições HTTP normais
    "websocket": AuthMiddlewareStack(  # Gerencia conexões WebSocket
        URLRouter(
            chat.routing.websocket_urlpatterns  # Usa as rotas WebSocket do chat
        )
    ),
})
