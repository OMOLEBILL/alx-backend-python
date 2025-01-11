from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """
    Model representing a message sent from one user to another.
    """
    sender = models.ForeignKey(
        User,
        related_name='sent_messages',
        on_delete=models.CASCADE,
        help_text="The user who sent the message."
    )
    receiver = models.ForeignKey(
        User,
        related_name='received_messages',
        on_delete=models.CASCADE,
        help_text="The user who will receive the message."
    )
    content = models.TextField(
        help_text="The content of the message."
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the message was created."
    )
    edited = models.BooleanField(
        default=False,
        help_text="Indicates whether the message has been edited."
    )

    def __str__(self):
        # Return a string representation of the message
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"


class Notification(models.Model):
    """
    Model representing a notification generated when a new message is received.
    """
    user = models.ForeignKey(
        User,
        related_name='notifications',
        on_delete=models.CASCADE,
        help_text="The user who will receive this notification."
    )
    message = models.ForeignKey(
        Message,
        related_name='notifications',
        on_delete=models.CASCADE,
        help_text="The message that triggered this notification."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the notification was created."
    )
    read = models.BooleanField(
        default=False,
        help_text="Indicates whether the notification has been read by the user."
    )

    def __str__(self):
        # Return a string representation of the notification
        return f"Notification for {self.user} about message {self.message.sender.username} -> {self.message.receiver.username}"
    
class MessageHistory(models.Model):
    """
    Model representing the history of edits for a message.
    """
    message = models.ForeignKey(
        Message,
        related_name='history',
        on_delete=models.CASCADE,
        help_text="The message that was edited."
    )
    old_content = models.TextField(help_text="The content of the message before the edit.")
    edited_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the message was edited."
    )

    def __str__(self):
        return f"History for Message {self.message.id} at {self.edited_at}"