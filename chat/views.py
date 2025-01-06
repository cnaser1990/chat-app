from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def chat_room(request, room_name):
    return render(request, 'chat.html', {'room_name': room_name})