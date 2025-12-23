from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "input")

    class Meta:
        model = User
        fields = ("email",)


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "input")
