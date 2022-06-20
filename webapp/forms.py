from django import forms
from .models import ContactDetails

class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields= ('firstname', 'lastname', 'email', 'comments')


    firstname = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='Email address', widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
    comments = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Write your message here', 'rows': 3})
    )
    