from django.shortcuts import render

from .models import Topic

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
