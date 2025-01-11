from django.db import models

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        # Filters messages by receiver=user and read=False,
        # then restricts the fields with .only() for efficiency.
        return self.filter(
            receiver=user,
            read=False
        ).only('id', 'sender', 'content', 'timestamp')