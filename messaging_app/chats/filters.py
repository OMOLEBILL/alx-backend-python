import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    """
    Filter messages by:
      - sender_id (exact match)
      - conversation_id (exact match)
      - sent_at >= sent_at_min
      - sent_at <= sent_at_max
    """
    sent_at_min = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='gte')
    sent_at_max = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='lte')

    class Meta:
        model = Message
        fields = [
            'sender_id',
            'conversation',
        ]
