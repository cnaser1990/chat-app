import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat.consumers import ChatConsumer  

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Define the ASGI application that handles both HTTP and WebSocket traffic
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
        ])
    ),
})
