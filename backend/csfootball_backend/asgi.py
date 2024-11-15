import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from notifications.routing import websocket_urlpatterns as notification_routes
from competitions.routing import websocket_urlpatterns as match_routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csfootball_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(notification_routes + match_routes)
    ),
})
