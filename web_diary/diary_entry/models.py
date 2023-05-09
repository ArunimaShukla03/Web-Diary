from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    # "User" is on the one side of the relationship and "Entry" is on the many side using ForeignKey. Therefore, for every User, there are many Entrys.

    # models.CASCADE signify that when the user is deleted all the entries associated with that user are also deleted.

    title = models.CharField(max_length=70, null=True, blank=True)
    mood = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField()

    # "models.SET_NULL" means that when you delete a particular mood, its value will get equal to null. And "blank=True" ensures that we can submit an empty field in the form.

    def __str__(self):
        return f"{self.date_created.date()}"