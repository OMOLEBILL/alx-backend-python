from django.contrib import admin
from .models import Message, Notification

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Message model.
    """
    list_display = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('timestamp',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Notification model.
    """
    list_display = ('user', 'message', 'created_at', 'read')
    search_fields = ('user__username', 'message__content')
    list_filter = ('created_at', 'read')
