from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signUpForm
from django.shortcuts import render

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

# 5. Segment Page
def segment(request):
    return render(request,'segment.html')

# 6. Project Page
def project(request):
    return render(request, 'project.html')


# 8. Segmented Output Page
def Segmented_output(request):
    return render(request,'seg_output.html')

# 9. logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out...")
    return redirect('home')

