from django import forms
from . models import Subscriber, MailMessage


class SubsciberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'
