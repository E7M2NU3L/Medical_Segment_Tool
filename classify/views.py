from django.shortcuts import render
from .forms import ClassifierForm
import numpy as np
from PIL import Image
import keras as ke
import os
# Create your views here.

# 4. Classify Page
def classify(request):
    form = ClassifierForm()

    if request.method == 'POST':
        # gettig the data from the form
        form = ClassifierForm(
            request.POST,
            request.FILES
        )    

        # printing the data for checking the quality
        print(request.POST)
        print(request.FILES)
        
        # getting the file
        image = form.cleaned_data.get('file')
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

        
        global val_classify 
        def val_classify():
            return config

        # return the configuration
        return render(request, 'classify.html', config)
    
    # config for the main section
    config = {
        'form': form,
        'img': None,
        'img_shape': None
    }

    return render(request, 'classify.html', config)

cur_path = os.getcwdb()
print(cur_path)

model = []
# model = ke.models.load_model('./models/classify.h5')
# 7. Classified output page
def Classified_output(request):
    data = val_classify()
    print(data)

    # getting the file and shape from the data
    img = data['img']
    shape = data['img_shape']

    # preict the output of the classifier
    classified_output = model.predict(np.array(img))

    print(classified_output)

    # decale new config
    configurations = {
        'image': img,
        'output': classified_output,
        'shape': np.array(shape),
    }

    return render(request, 'class_output.html', configurations)