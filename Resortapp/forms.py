from django import forms
from . models import Contacts, Members
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class contact_form(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = "__all__"

class member_form(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'
        
class formsingup(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2"]
