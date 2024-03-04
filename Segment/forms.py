from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import FileConvert

class signUpForm(UserCreationForm):
    email = forms.EmailField(label = "", widget = forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder': 'email'}
    ))

    first_name = forms.CharField(
        label ="",
        max_length= 100,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'first_name'
            }
        )
    )

    last_name = forms.CharField(
        label ="",
        max_length= 100,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'last_name'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'password1', 'password2'
        )
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(signUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['email'].label = ""
        self.fields['email'].help_text = "<span class='form-text text-muted'><small class='text-white'>Required</small></span>"

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = "<ul class='form-text text-muted'><small class = 'text-white'>Required</small></ul>"

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = "<span class='form-text text-muted'><small class='text-white'>Required</small><br /><ul><li>The Password must be atleast of 8 characters</li><li>It must use literals like $, &, !,  @ etc.,</li><li>Don't use your Email id as password</li></ul></span>"


class DicomConvert(forms.ModelForm):
    class Meta:
        model = FileConvert
        fields = ['file']