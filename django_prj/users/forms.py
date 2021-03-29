from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField
from django import forms
from django.contrib.auth.models import User
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email ID")
    # phone = PhoneField(required=False,max_length = 10)
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
