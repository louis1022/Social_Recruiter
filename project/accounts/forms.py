from django import forms
from .models import Introduce

class IntroduceForm(forms.ModelForm):

    class Meta:
        model = Introduce
        fields = ("company_name","recruiter",)
