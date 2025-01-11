from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

@login_required
def delete_user(request):
    """
    View that allows a logged-in user to delete their account.
    """
    user = request.user

    if request.method == 'POST':
        # Confirm deletion
        user.delete()             # This triggers the post_delete signal
        logout(request)          # Log the user out after deletion
        return redirect('home')  # Redirect to a homepage 

    # On GET, show a confirmation page
    return render(request, 'templates/confirm_delete_account.html', { 'user': user })
