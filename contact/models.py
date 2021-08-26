from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AdressEntery(models.Model):
    MALE = 'm'
    FAMELE = 'f'
    # fix '1' error for choices 'choices' must be an iterable containing (actual value, human readable name) tuples django 3.1
    CHOICES_GENDER = [
        ('MALE', "Male"),
        ('FAMELE', 'Famele')
    ]
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adressentery", null=True) #represents the user who is logged in and when creating a contact we assign the user name
    name = models.CharField(max_length = 120)
    gender = models.CharField(max_length=9, choices=CHOICES_GENDER)
    birthDate = models.DateField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    person = models.ForeignKey(AdressEntery, on_delete=models.CASCADE)
    firstName = models.CharField(max_length = 120)
    lastName = models.CharField(max_length = 120)

    def __str__(self):
        return str(self.person)

class Contact(models.Model):
    contact = models.ForeignKey(AdressEntery, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField()

    def __str__(self):
        return str(self.contact)
    #region fix
    # This is the way we display our data from the table located in the admin panel,
    #  and the shell in the docker container will not be returned to us anymore (table name objects (1))
    #endregion

   # name  gender  birthDate  active firstName lastName phoneNumber