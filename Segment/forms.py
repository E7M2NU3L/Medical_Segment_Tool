from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import FileConvert
from .models import Classify

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

    FileName = forms.CharField(
        label ="",
        max_length= 100,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'FileName'
            }
        )
    )

    file = forms.FileField(
        label ="",
        widget= forms.FileInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'file'
            }
        )
    )

    class Meta:
        model = FileConvert
        fields = ['file']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(DicomConvert, self).__init__(*args, **kwargs)  # Corrected super call

        self.fields['FileName'].widget.attrs['class'] = 'form-control'
        self.fields['FileName'].widget.attrs['placeholder'] = 'FileName'
        self.fields['FileName'].label = ""
        self.fields['FileName'].help_text = "<span class='form-text text-muted'><small class='text-white'>Required</small></span>"

        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['placeholder'] = 'file'
        self.fields['file'].label = ""
        self.fields['file'].help_text = "<span class='form-text text-muted'><small class='text-white'>Required</small></span><br /><hr /><h3>Points to Notice</h3><br /><ul><li>The Dicom file must be uncorrupted, proper image acquisition</li><br /><li>The image file must be less than 2 MB</li><li>Click the submit button to upload</li><li>Keep a unique name for the Image or File e.g. patient_00_123 etc.,</li></ul>"

class ClassifierForm(forms.ModelForm):
    # file name for classification
    fileName = forms.CharField(
        label= "",
        max_length= 100,
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder': 'mri-11-02-2009.dcm'
            }
        )
    )

    # file as input
    file = forms.FileField(
        label="",
        widget= forms.FileInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Select'
            }
        )
    )

    class Meta:
        model = Classify
        fields = ['file_classify']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ClassifierForm, self).__init__(*args, **kwargs)  # Corrected super call

        self.fields['fileName'].widget.attrs['class'] = 'form-control'
        self.fields['fileName'].widget.attrs['placeholder'] = 'FileName'
        self.fields['fileName'].label = ""
        self.fields['fileName'].help_text = "<span class='form-text text-muted'><small class='text-white'>Required</small></span>"

        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['placeholder'] = 'Select'
        self.fields['file'].label = ""
        self.fields['file'].help_text = "<span class='form-text text-muted'><small class='text-white'>Required</small></span><br /><hr /><h3>Points to Notice</h3><br /><ul><li>The Dicom file must be uncorrupted, proper image acquisition</li><br /><li>The image file must be less than 2 MB</li><li>Click the submit button to upload</li><li>Keep a unique name for the Image or File e.g. patient_00_123 etc.,</li></ul>"
