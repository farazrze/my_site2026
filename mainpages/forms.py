from django import forms
from mainpages.models import Contact,newsletter
from captcha.fields import CaptchaField


class Contact_form(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = Contact
        fields ="__all__"


class newsletter_form(forms.ModelForm):

    class Meta:
        model = newsletter
        fields = "__all__"