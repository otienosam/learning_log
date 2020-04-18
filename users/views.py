from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):

    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()#instance with no Initial data
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)#instance with
        #submitted data

        if form.is_valid():
            new_user = form.save()#save the username and the hash of the
            # password to the database

            # Log the user in and then redirect to home page.
            login(request, new_user)#creates a valid session for the new user
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
