from rest_framework.permissions import BasePermission

class IsConversationParticipant(BasePermission):
    """
    Custom permission to check if the requesting user is a participant of the conversation.
    """

    def has_object_permission(self, request, view, obj):
        # 'obj' is a Conversation instance
        # Check if this user is the same as the conversation's participants_id
        return obj.participants_id == request.user


class IsMessageSender(BasePermission):
    """
    Custom permission to ensure that the requesting user is the sender of the message.
    """

    def has_object_permission(self, request, view, obj):
        # 'obj' is a Message instance
        return obj.sender_id == request.user
