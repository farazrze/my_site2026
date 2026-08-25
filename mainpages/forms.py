from django import forms
from mainpages.models import Contact,newsletter


class Contact_form(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields ="__all__"


class newsletter_form(forms.ModelForm):

    class Meta:
        model = newsletter
        fields = "__all__"