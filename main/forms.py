from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import UserProfile


class BirdForm(forms.Form):
    name = forms.CharField()


class NewUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# https://github.com/rkorzen/panopt

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["bio"]


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)