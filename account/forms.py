from django import forms
from django.contrib.auth.models import User
from .models import Profile
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'Enter your password'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                    'placeholder':'Enter your password'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
             widget=forms.PasswordInput(attrs={'class':'form-control',
                                   }))
    password2 = forms.CharField(label='Repeat password',
             widget=forms.PasswordInput(attrs={'class':'form-control',
                                    'placeholder':'Enter your password'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')