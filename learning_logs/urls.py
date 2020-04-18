"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'# variable to distinguish this urls.py file from
#files of the same name in other apps within the project
urlpatterns = [
# Home page
path('', views.index, name='index'),
#the empty string matches the base url which is ignored. Any other url wont match
#this url.A page is given whenever requested url doesn't match existing ones
# views.index argument speccifies to call the index function from the view module
#the third argument provides the name index for this URL pattern so we can
#refer to it in other code sections

# Page that shows all topics.
path('topics/', views.topics, name='topics'),
# Detail page for a single topic.
path('topics/<int:topic_id>/', views.topic, name='topic'),
# Page for adding a new topic
path('new_topic/', views.new_topic, name='new_topic'),
# Page for adding a new entry
path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
# Page for editing an entry.
path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
