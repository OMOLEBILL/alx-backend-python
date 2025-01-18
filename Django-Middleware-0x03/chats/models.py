from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    """"
      user_id          (Primary Key, UUID, Indexed)
      first_name       (VARCHAR, NOT NULL)
      last_name        (VARCHAR, NOT NULL)
      email            (VARCHAR, UNIQUE, NOT NULL)
      password_hash    (VARCHAR, NOT NULL)
      phone_number     (VARCHAR, NULL)
      role             (ENUM: 'guest', 'host', 'admin', NOT NULL)
      created_at       (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
    """
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password_hash = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ROLE_CHOICES = (
        ('guest', 'guest'),
        ('host', 'host'),
        ('admin', 'admin'),
    )
    role = models.CharField(
        max_length=5,
        choices=ROLE_CHOICES,
        null=False,
        blank=False
    )

    class Meta:
        indexes = [
            models.Index(fields=['user_id'])
        ]

    def __str__(self):
        return self.username
    
class Conversation(models.Model):
    """
      conversation_id   (Primary Key, UUID, Indexed)
      participants_id   (Foreign Key, references User(user_id))
      created_at        (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
    """
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['conversation_id'])
        ]

    def __str__(self):
        return  f"Conversation {self.id}"
    
class Message(models.Model):
    """
      message_id       (Primary Key, UUID, Indexed)
      sender_id        (Foreign Key, references User(user_id))
      message_body     (TEXT, NOT NULL)
      sent_at          (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
    """
    
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages', null=True,  blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['message_id'])
        ]

    def __str__(self):
        return f"Message {self.id} from {self.sender.username}"
