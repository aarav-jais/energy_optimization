from django import forms
from .models import RenewableEnergyGeneration
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class RenewableEnergyGenerationForm(forms.ModelForm):
    class Meta:
        model = RenewableEnergyGeneration
        fields = ['source', 'amount_generated']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)
    department = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
