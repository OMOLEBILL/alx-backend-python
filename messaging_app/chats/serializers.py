from rest_framework import serializers
from .models import user, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the custom `user` model, including all fields you specified.
    """
    class Meta:
        model = user
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'password_hash',
            'phone_number',
            'role',
            'created_at',
            'username', 
        ]


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializes the `Message` model, showing both the sender (nested user)
    and (optionally) the conversation if you added that ForeignKey.
    """

    # Nest the sender info. By default, this is read-only if you just want to display it.
    sender = UserSerializer(source='sender_id', read_only=True)

    class Meta:
        model = Message
        fields = [
            'message_id',
            'sender_id',     
            'sender',     
            'message_body',
            'sent_at'
            'conversation' 
        ]


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializes the `Conversation` model, optionally including nested messages
    and the participant user data.
    """

    # Nest the participant info
    participant = UserSerializer(source='participants_id', read_only=True)

    # If you have a `conversation` FK in Message, then you can nest messages:
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants_id',  
            'participant', 
            'created_at',
            'messages'        
        ]
