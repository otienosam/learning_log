from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)#data that’s made up of characters,
    # or text
    date_added = models.DateTimeField(auto_now_add=True)#automatically set
    #to the current date and time whenever the user creates a new topic.

    def __str__(self):#diplays simple representation of a model
        """Return a string representation of the model."""
        return self.text
#Whenever we want to modify the data that Learning Log manages, we’llfollow
# these three steps:
     # modify models.py,
     # call makemigrations on learning_logs ,
     #and tell Django to migrate the project.
class Entry(models.Model):
    """Something specific learned about a topic."""
    #connects each entry to a specific topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#foreign key instance
    #The on_delete=models.CASCADE argument tells Django that when a topic
    #is deleted, all the entries associated with that topic should be
    #deleted as well
    text = models.TextField()#instanceof TextField
    date_added = models.DateTimeField(auto_now_add=True)#allows presentation of
    #entries in the order they were created and to place a timestamp next to
    #each entry.

    class Meta:
        #nested class to hold extra information for managing a model
        verbose_name_plural = 'entries'#used when there is need to refer
        #to more than one entry by django

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
