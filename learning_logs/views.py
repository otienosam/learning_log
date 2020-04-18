from django.shortcuts import render,redirect

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')#the first argument is the
    #original request object and the second is the template to use webpages

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')#database querried to retrieve
    #topic
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)#query to the database
    entries = topic.entry_set.order_by('-date_added')#another query to the database
    #The minus sign in front of date_added sorts the results in reverse
    # order diplaying the recent entries first
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()#blamk form that the users can fill
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():#a function to check that the entered data is
        #valid
            form.save()#the save function writes to the datatbase
            return redirect('learning_logs:topics')#leave the page after
            #filling in the form

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
    #runs  if the form is blamk or the submitted data is invalid

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)#create a new entry object and
            #assign it to new_entry without saving it to the database yet
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
            #topic_id is the argument required by view function.Its needed
            #by topic()

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
        #instance argument tells Django to create the form prefilled with
        #information from the existing entry object.
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        #arguments tell Django to create a form instance based on the
        #information associated with the existing entry objec ,updated with
        #any relevant data from request.POST
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
