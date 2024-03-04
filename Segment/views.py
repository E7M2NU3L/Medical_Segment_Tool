from django.shortcuts import render
import numpy as np
import png
import pydicom

# Create your views here.
# 1. Home page
def home(request):
    return render(request, 'index.html')

# 2. Login Page
def login(request):
    return render(request, 'login.html')

# 3. Register Page
def register(request):
    return render(request,'signup.html')

# 4. Classify Page
def classify(request):
    return render(request, 'classify.html')

# 5. Segment Page
def segment(request):
    return render(request,'segment.html')

# 6. Project Page
def project(request):
    return render(request, 'project.html')

# 7. Classified output page
def Classified_output(request):
    return render(request, 'class_output.html')

# 8. Segmented Output Page
def Segmented_output(request):
    return render(request,'seg_output.html')

def convert_dcm_to_jpg(request):
    ds = pydicom.dcmread("./MyImage.dcm")
    shape = ds.pixel_array.shape
    # Convert to float to avoid overflow or underflow losses.
    image_2d = ds.pixel_array.astype(float)
    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 256
    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)
    # Write the PNG file
    with open("out.png", 'wb') as png_file:
        w = png.Writer(shape[1], shape[0], greyscale=True)
        w.write(png_file, image_2d_scaled)

    # config
    config = {
        "image": png_file
    }
    return render(request, 'file_converter.html', config)