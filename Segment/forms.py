from typing import Any, Mapping
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Segment 

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

class SegmentForm(forms.ModelForm):

    # get the criteria for the data to be passed
    
    # 1. Name of the file to be passed
    FileName = forms.CharField(
        label="",
        max_length=100,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Name the file',
            }
        )
    )

    # 2. File Upload
    File = forms.FileField(
        label="",
        widget= forms.FileInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    # defining the html for the fields
    class Meta:
        Model = Segment
        fields = ['FileName', 'File']

    # defining the init function
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SegmentForm, self).__init__(*args, **kwargs)

        self.fields['FileName'].widget.attrs['class'] = 'form-control'
        self.fields['FileName'].widget.attrs['placeholder'] = 'Name the file'
        self.fields['FileName'].label = ""
        self.fields['FileName'].help_text = "<span class='form-text text-muted'><small class='text-white'>Required</small></span><br /><hr /> <ul><li>The File must ne named according to the patient's unique id or DOBs etc.,</li><li>The naming of the file is adviced not to use patient's original name</li></ul>"

        self.fields['File'].widget.attrs['class'] = 'form-control'
        self.fields['File'].widget.attrs['placeholder'] = 'Name the file'
        self.fields['File'].label = ""
        self.fields['File'].help_text = "<span class='form-text text-muted'><small class='text-white'>Required</small></span><br /><hr /> <ul><li>The model is not accuracte enough to make real time segmentations.</li><li>Segment the same data i.e., the images two to three times to find the repetability and correct prediction of the model</li><li>The Segmentation will take about 3 to 4 minutes to complete</li></ul>"







