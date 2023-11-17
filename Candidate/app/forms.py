from django import forms
from .models import Candidatedirectory

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidatedirectory
        fields = '__all__'
