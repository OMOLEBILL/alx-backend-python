from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.db import models
from .models import Message

@login_required
def delete_user(request):
    """
    View that allows a logged-in user to delete their account.
    """
    user = request.user

    if request.method == 'POST':
        # Confirm deletion
        user.delete()            # This triggers the post_delete signal
        logout(request)          # Log the user out after deletion
        return redirect('home')  # Redirect to a homepage 

    # On GET, show a confirmation page
    return render(request, 'templates/confirm_delete_account.html', { 'user': user })


def fetch_threaded_replies(message):
    """
    Recursively fetches all replies to a given message,
    building a nested structure representing the thread.
    """
    # Prefetch replies for the current message (should already be prefetched if optimized)
    replies = list(message.replies.all())
    # For each reply, recursively fetch its replies
    for reply in replies:
        reply.threaded_replies = fetch_threaded_replies(reply)
    return replies

def message_thread_view(request, message_id):
    root_message = get_object_or_404(
        Message.objects.filter(id=message_id).filter(
            models.Q(sender=request.user) | models.Q(receiver=request.user)
        ).select_related('sender', 'receiver').prefetch_related(
            'replies',
            'replies__sender',
            'replies__receiver'
        ),
        id=message_id
    )

    # Build the nested thread structure recursively
    threaded_replies = fetch_threaded_replies(root_message)

    context = {
        'root_message': root_message,
        'threaded_replies': threaded_replies,
    }
    return render(request, 'templates/message_thread.html', context)


@login_required
def inbox_view(request):
    """
    Display the inbox with only unread messages for the logged-in user.
    """
    #.only('id', 'sender', 'content', 'timestamp')
    unread_messages = Message.unread.unread_for_user(request.user)

    context = {
        'unread_messages': unread_messages
    }
    return render(request, 'templates/inbox.html', context)


@cache_page(60)
def conversation_list_view(request):
    """
    A view that lists messages in a conversation.
    This view is cached for 60 seconds using the cache_page decorator.
    """
    
    context = {'example': 'Messages would be listed here...'}
    return render(request, 'conversation_list.html', context)