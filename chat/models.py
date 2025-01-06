from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

# Extend the default User model to include custom fields
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    is_online = models.BooleanField(default=False)

# Chat Room Model
class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(get_user_model(), related_name='chatrooms')
    created_at = models.DateTimeField(auto_now_add=True)

# Message Model
class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)