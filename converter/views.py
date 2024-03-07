from django.shortcuts import render, redirect
from django.contrib import messages
import pydicom
import numpy as np
from PIL import Image
from .forms import DicomConvert

# Create your views here.
# convert Code
def convert(request):
    form1 = DicomConvert()
    img = None  # Initialize img to None

    if request.method == 'POST':
        form1 = DicomConvert(
            request.POST,
            request.FILES
        )
        if form1.is_valid():
            # dicom file from the request
            dicom_file = form1.cleaned_data.get('file')
            request_file = request.FILES
            # read the dicom file
            dicom_image = pydicom.dcmread(dicom_file | request_file)  # This line may need adjustment
            # get the shape of the image
            dicom_shape = dicom_image.pixel_array.shape
            # convert to float
            dicom_image.pixel_array = dicom_image.pixel_array.astype(float)
            # rescale grey scale between 0-255
            dicom_image.pixel_array = (np.maximum(dicom_image.pixel_array,0) / dicom_image.pixel_array.max()) * 256
            # convert to uint
            dicom_image.pixel_array = np.uint8(dicom_image.pixel_array)
            # write the png file
            img = Image.fromarray(dicom_image.pixel_array)
            # save the image
            img.save("./images/converted/img.png")
            # save the form
            form1.save()
            messages.success(request, "You have successfully converted the Dicom file to a png file...")
            return redirect('home')
        
        else:
            config = {
                'form': form1, 
                'image': img,
                'dicom_file' : dicom_file
            }
            return render(request, 'convert.html', config)
        
    return render(request, 'convert.html', {
        'form': form1,
        'image': img,
        'dicom_file' : None  # Provide a default value for dicom_file
    })

def converted_image(request):
    return render(request, 'converted_image.html')