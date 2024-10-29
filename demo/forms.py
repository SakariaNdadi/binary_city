from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            "name",
            "surname",
            "email",
        )


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ("name",)
