from django import forms
from .models import Message,Introduce
from django.core.mail import send_mail
from django.conf import settings

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

class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        message = self.cleaned_data['message']
        from_email = settings.EMAIL_HOST_USER
        to = [settings.EMAIL_HOST_USER]

        send_mail("問い合わせ", message, from_email, to)
