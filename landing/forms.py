from django import forms
from weatherapp.models import Bb

class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'image')