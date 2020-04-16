from django.contrib import admin

# Register your models here.
from .models import Topic#The dot in front of models tells Django to look for
# models.py in the same directory as admin.py

admin.site.register(Topic)# mean manage our model through the admin site
