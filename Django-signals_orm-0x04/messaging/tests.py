from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessageNotificationTestCase(TestCase):
    def setUp(self):
        """
        Set up test users and initial data for each test.
        """
        self.sender = User.objects.create_user(username='sender_user', password='password')
        self.receiver = User.objects.create_user(username='receiver_user', password='password')

    def test_notification_created_on_message(self):
        """
        Test that a notification is automatically created when a new message is sent.
        """
        # Create a new message from sender to receiver
        msg = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Hello, this is a test message!'
        )

        # Fetch notifications for the receiver
        notifications = Notification.objects.filter(user=self.receiver)

        # Assert that exactly one notification was created
        self.assertEqual(notifications.count(), 1)

        # Further assert that the notification is linked to the correct message
        notification = notifications.first()
        self.assertEqual(notification.message, msg)
        self.assertFalse(notification.read, "Notification should initially be unread")
