from django import forms
from .models import Classify
from typing import Any

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
        fields = ['file']

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
