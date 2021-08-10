from django.db import models

# Create your models here.
class AdressEntery(models.Model):
    MALE = 'm'
    FAMELE = 'f'
    # fix '1' error for choices 'choices' must be an iterable containing (actual value, human readable name) tuples django 3.1
    CHOICES_GENDER = [
        (MALE, "Male"),
        (FAMELE, 'Famele')
    ]
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    name = models.CharField(max_length = 120)
    gender = models.CharField(max_length=9, choices=CHOICES_GENDER)
    birthDate = models.DateField()
    active = models.BooleanField(default=True)
    # if choices does not work uncommit
    # def is_superclass(self):
    #     return self.CHOICES_GENDER in {self.MALE, self.FAMELE}

class Person(models.Model):
    person = models.ForeignKey(AdressEntery, on_delete=models.CASCADE)
    firstName = models.CharField(max_length = 120)
    lastName = models.CharField(max_length = 120)

class Contact(models.Model):
    contact = models.ForeignKey(AdressEntery, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField()