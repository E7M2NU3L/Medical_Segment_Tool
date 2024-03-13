import os
import pydicom
from PIL import Image

def convert_dicom_to_jpg(dicom_dir, jpg_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(jpg_dir):
        os.makedirs(jpg_dir)

    # Loop through all files in the DICOM directory
    for filename in os.listdir(dicom_dir):
        print(filename)
        if filename.endswith(".dcm"):
            # Read the DICOM file
            ds = pydicom.dcmread(os.path.join(dicom_dir, filename))
            
            # Convert pixel array to image
            image = Image.fromarray(ds.pixel_array)
            
            # Save the image as JPEG
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            image.save(os.path.join(jpg_dir, jpg_filename))

if __name__ == "__main__":
    # Set the directory containing DICOM files and directory to save JPEGs
    dicom_directory = "E://Ruth_Final_Project/Dataset/images"
    jpg_directory = "E://Ruth_Final_Project/Dataset_Converted/images"

    # Convert DICOM to JPEG
    convert_dicom_to_jpg(dicom_directory, jpg_directory)
