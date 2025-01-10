from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_notification_for_new_message(sender, instance, created, **kwargs):
    """
    Signal handler that automatically creates a Notification when a new Message is saved.
    
    This function listens for the post_save signal from the Message model.
    
    Parameters:
    - sender: The model class sending the signal (Message).
    - instance: The actual instance of Message that was saved.
    - created: A boolean; True if a new record was created.
    - kwargs: Additional keyword arguments.
    """
    # Only create a notification if a new Message was created
    if created:
        # Create a new notification for the receiver of the message
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )