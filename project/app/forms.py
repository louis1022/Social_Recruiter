from django import forms
from .models import Message
from social_django.models import UserSocialAuth

# class MessageForm(forms.Form):
#     message = forms.CharField(label='message', max_length=10000)
class MessageForm(forms.ModelForm):

    class Meta:
        model = Message # どのモデルからformつくる？
        fields = ('message',) # どのフィールドこのformで使う
