from django.contrib import admin
from .models import ChatRoom, Message


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'created_at']
    list_filter = ['created_at']
    search_fields = ['patient__user__username', 'doctor__user__username']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_room', 'sender', 'created_at']
    list_filter = ['created_at']
    search_fields = ['chat_room__id', 'sender__username']
