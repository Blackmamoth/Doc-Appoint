from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class AppointmentForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'checkup_for']
