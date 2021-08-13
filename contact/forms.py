from django import forms

class CreateContact(forms.Form):    #the form contains fields that must be filled in to create a contact
    GENDER_CHOICES =(
    ("1", "Male"),
    ("2", "Famele"),
)   # values of Choice Field
    YEARS =[x for x in range(1940,2022)] #beginning and end of year counting

    name = forms.CharField(label="name", max_length = 120, widget = forms.TextInput(attrs={'placeholder':'Enter name'}))
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    birthDate = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    firstName = forms.CharField(max_length = 120, widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    lastName = forms.CharField(max_length = 120, widget = forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    phoneNumber = forms.IntegerField(widget = forms.TextInput(attrs={'placeholder':'Enter phone number'}))

class OptionalForm(forms.Form): #an endpoint update form that contains fields that are not required to be filled in and one value can be changed e.g. name
    GENDER_CHOICES =(
    ("1", "Male"),
    ("2", "Famele"),
)
    YEARS =[x for x in range(1940,2022)]

    name = forms.CharField(label="name", max_length = 120, required=False ,widget = forms.TextInput(attrs={'placeholder':'Enter name'}))
    gender = forms.ChoiceField(choices = GENDER_CHOICES, required=False)
    birthDate = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), required=False)
    firstName = forms.CharField(max_length = 120, required=False ,widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    lastName = forms.CharField(max_length = 120, required=False ,widget = forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    phoneNumber = forms.IntegerField(widget = forms.TextInput(attrs={'placeholder':'Enter phone number'}),required=False)