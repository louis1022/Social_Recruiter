from django import forms
from .models import Message,Introduce

# class MessageForm(forms.Form):
#     message = forms.CharField(label='message', max_length=10000)
class MessageForm(forms.ModelForm):

    class Meta:
        model = Message # どのモデルからformつくる？
        fields = ('message',) # どのフィールドこのformで使う

class IntroduceForm(forms.ModelForm):

    class Meta:
        model = Introduce
        fields = ("company_name","recruiter",)
