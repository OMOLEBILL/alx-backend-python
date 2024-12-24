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

class IsParticipantOfConversation(BasePermission):
    """
    Allows access only to participants of the conversation for viewing,
    creating, updating, or deleting messages and conversations.
    Assumes:
      - Conversation has a field: participants (ManyToMany) or participants_id (ForeignKey)
      - Message links to a Conversation via 'conversation' FK or
        we can retrieve conversation from obj if it's already a Conversation instance.
    """

    def has_object_permission(self, request, view, obj):
        """
        If `obj` is a Conversation, check if request.user is in participants.
        If `obj` is a Message, check if request.user is in the conversation participants.
        """
        # Identify the conversation object
        if hasattr(obj, 'participants'):  
            return obj.participants_id == request.user

        if hasattr(obj, 'conversation'):
            conversation = obj.conversation
            return conversation.participants_id == request.user


        return False