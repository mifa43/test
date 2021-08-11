from django import forms

class CreateContact(forms.Form):
    GENDER_CHOICES =(
    ("1", "Male"),
    ("2", "Famele"),
)
    YEARS =[x for x in range(1940,2022)]

    name = forms.CharField(label="name", max_length = 120, widget = forms.TextInput(attrs={'placeholder':'Enter name'}))
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    birthDate = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    firstName = forms.CharField(max_length = 120, widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    lastName = forms.CharField(max_length = 120, widget = forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    phoneNumber = forms.IntegerField(widget = forms.TextInput(attrs={'placeholder':'Enter phone number'}))