from rest_framework import serializers
from .models import ChatRoom, Message, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'is_online']

class ChatRoomSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'members', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'content', 'timestamp', 'is_read', 'file']