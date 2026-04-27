from django import forms
from .models import Film
from datetime import date

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        
  


def clean_date_sortie(self):
    date_sortie = self.cleaned_data.get('date_sortie')

    # إلا كانت فارغة
    if date_sortie is None:
        return date_sortie

    # تحقق من المستقبل
    if date_sortie > date.today():
        raise forms.ValidationError("La date de sortie ne doit pas être dans le futur.")

    return date_sortie      