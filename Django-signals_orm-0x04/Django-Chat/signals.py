from django.db.models.signals import pre_save
from django.dispatch import receiver
from .Models import Message, MessageHistory

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

            # Create a history record for the old content
            MessageHistory.objects.create(
                message=old_message,
                old_content=old_message.content
            )
