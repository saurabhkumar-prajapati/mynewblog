from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from.models import Post

class SignUPForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name =forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': "form-control",}),
                   #'first_name': forms.TextInput(attrs={'class': "form-control",}),
                   #'last_name': forms.TextInput(attrs={'class': "form-control",}),
                   #'email': forms.EmailInput(attrs={'class': "form-control",})
                   } #required true not working in widget here


class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': "form-control"}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs=
                                             {'autocomplete':'current-password', 'class': "form-control"}))

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc']
        labels={'title':'Title','desc':"Description"}
        widgets={'title':forms.TextInput(attrs={"class":'form-control'}),'desc':forms.Textarea(attrs=
                                        {'class':'form-control'}),}

class ContactForm(forms.Form):

        first_name = forms.CharField(label="First Name" ,widget=forms.TextInput(attrs={'class': "form-control"}))
        last_name = forms.CharField(label="Last Name" ,widget=forms.TextInput(attrs={'class': "form-control"}))
        contact_number=forms.CharField(label="Contact Number",widget=forms.TextInput(attrs={'class': "form-control"}))
        email_address = forms.EmailField(label="Email Address",widget=forms.TextInput(attrs={'class': "form-control"}))
        message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'max_length':2000}))

        #is not working (may be only for modalform) widgets = {
                  # 'first_name': forms.TextInput(attrs={'class': "form-control"}),
                   #'last_name': forms.TextInput(attrs={'class': "form-control"}),
                  # 'email_address': forms.EmailInput(attrs={'class': "form-control"}),


