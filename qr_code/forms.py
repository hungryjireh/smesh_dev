from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import QrcodeImage

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class LinksForm(forms.Form):
    facebook_link = forms.CharField(required=False)
    linkedin_link = forms.CharField(required=False)
    resume_link = forms.CharField(required=False)
    github_link = forms.CharField(required=False)
    twitter_link = forms.CharField(required=False)
    pinterest_link = forms.CharField(required=False)
    portfolio_link = forms.CharField(required=False)
    instagram_link = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    email_address = forms.CharField(required=False)

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = QrcodeImage
        fields = ['image']

class InteractionNotesForm(forms.Form):
    interaction_notes = forms.CharField(widget=forms.Textarea, required=False)
