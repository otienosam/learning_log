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
