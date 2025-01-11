from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

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

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    """
    Signal handler that logs the old content of a Message before it's edited.

    This function listens for the pre_save signal on the Message model.
    """
    # If the instance has a primary key, it already exists in the database.
    if instance.pk:
        try:
            # Retrieve the existing message from the database
            old_message = Message.objects.get(pk=instance.pk)
        except Message.DoesNotExist:
            # If the message doesn't exist, there's nothing to log.
            return

        # Check if the content has changed
        if old_message.content != instance.content:
            # Mark the message as edited
            instance.edited = True

            # Attempt to retrieve the user who edited the message
            # This assumes `instance._edited_by` was set before saving.
            edited_by = getattr(instance, '_edited_by', None)

            # Create a history record for the old content
            MessageHistory.objects.create(
                message=old_message,
                old_content=old_message.content,
                edited_by=edited_by
            )

@receiver(post_delete, sender=User)
def cleanup_user_related_data(sender, instance, **kwargs):
    """
    Signal handler that cleans up related data when a user is deleted.
    
    Deletes messages, notifications, and message histories associated with the user.
    """
    user = instance

    # Delete messages where the user is sender or receiver
    Message.objects.filter(sender=user).delete()
    Message.objects.filter(receiver=user).delete()

    # Delete notifications for the user
    Notification.objects.filter(user=user).delete()

    # Delete message histories related to messages by the user
    MessageHistory.objects.filter(message__sender=user).delete()
    MessageHistory.objects.filter(message__receiver=user).delete()