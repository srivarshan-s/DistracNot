from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app.consumer import StudentConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", StudentConsumer.as_asgi()),
    ])
})
