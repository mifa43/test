from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class NoteEntery(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notentery", null=True) #represents the user who is logged in and when creating a contact we assign the user name
    title = models.CharField(max_length = 120)
    note = models.CharField(max_length = 400)
    date = models.DateField()   ##notification date
    time = models.TimeField(null=True)  #notification time
    def __str__(self):
        return self.title