from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signUpForm
from .forms import DicomConvert
from .forms import ClassifierForm
from django.shortcuts import render
import numpy as np 
from PIL import Image
import pydicom

# Create your views here.
# 1. Home page
def home(request):
    return render(request, 'index.html')

# 2. Login Page
def login_user(request):

    # getting the Data
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # authenticate
        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been loggedin Successfully")
            return redirect('home')
        
        else:
            messages.error(request, "There was an error logging in...")
            return redirect('home')
        
    return render(request, 'login.html', {})

# 3. Register Page
def register(request):

    # getting the data
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password= raw_password)
            login(request, user)
            messages.success(request, "You have been registered Successfully")
            return redirect('home')
    else:
        form = signUpForm()
        config = {
            'form': form
        }
        return render(request,'signup.html', 
            config
        )
    
    return render(request,'signup.html', {'form': form})

# 4. Classify Page
def classify(request):
    form = ClassifierForm()

    if request.method == 'POST':
        # gettig the data from the form
        form = ClassifierForm(
            request.POST,
            request.FILES
        )    
        
        # getting the file
        image = form.cleaned_data.get('file_classify')
        file_alternate = request.FILES

        # convert the image to an numpy array
        if image is not None:
            img = np.array(Image.open(image))
        else:
            img = np.array(Image.open(file_alternate['file_alternate']))
        
        # pre processing
        trained_image = img.astype(np.float32) / 255.0

        # shape of the image
        img_shape = trained_image.shape

        # saving the form
        form.save()
        
        # configuration to be passed on
        config = {
            'form': form,
            'img': img,
            'img_shape': img_shape
        }

        # return the configuration
        return render(request, 'classify.html', config)
    
    # config for the main section
    config = {
        'form': form,
        'img': None,
        'img_shape': None
    }
    return render(request, 'classify.html', config)

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

# 9. logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out...")
    return redirect('home')

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