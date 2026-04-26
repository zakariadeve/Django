from django import forms
from .models import Film

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'   