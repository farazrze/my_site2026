from django import forms
from blog.models import Comment


class Comments_form(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ["name","post","email","subject","message"]

