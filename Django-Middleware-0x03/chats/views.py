from django.shortcuts import render
from rest_framework import viewsets, status, filters, permissions
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter 

class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving, updating, or deleting conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]

    # allow searching conversations by conversation_id
    filter_backends = [filters.SearchFilter]
    search_fields = ['conversation_id'] 

    def create(self, request, *args, **kwargs):
        """
        Override create() to add custom validation logic.
        """
        participants_id = request.data.get("participants_id", None)
        if not participants_id:
            return Response(
                {"detail": "participants_id is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)
    
    def get_queryset(self):
        # Ensure only conversations where the user is the participant
        return super().get_queryset().filter(participants_id=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving, updating, or deleting messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation, permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MessageFilter

    ordering_fields = ['sent_at']
    ordering = ['-sent_at']

    def create(self, request, *args, **kwargs):
        """
        Override create() to handle custom response status codes.
        Example scenario:
          - If the `sender_id` or `message_body` is missing, return 400.
        """
        sender_id = request.data.get("sender_id")
        message_body = request.data.get("message_body")

        if not sender_id or not message_body:
            return Response(
                {"detail": "sender_id and message_body are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        response = super().create(request, *args, **kwargs)
        response.data["message"] = "Message created successfully!"
        response.status_code = status.HTTP_201_CREATED
        return response
    
    def get_queryset(self):
        """
        If a conversation_pk is present (from the nested route),
        return only messages for that conversation.
        Otherwise, return all messages.
        """
        conversation_id = self.kwargs.get('conversation_pk')
        if conversation_id:
            return self.queryset.filter(conversation_id=conversation_id)
        return super().get_queryset().filter(conversation__participants_id=self.request.user)
