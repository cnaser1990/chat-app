from django.urls import path
from . import views, consumers

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]