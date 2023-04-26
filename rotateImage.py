from scipy import ndimage, misc
import numpy as np
import os
import cv2
import imageio
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sreek\OneDrive\Documents\OCR\tesseract' 

def main():
    outPath = r"C:\Users\Sreekanth\Desktop\OCR-Thermodata\rotatedimages"
    path = r"C:\Users\Sreekanth\Desktop\OCR-Thermodata\data"

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        image_to_rotate = imageio.imread(input_path)

        # rotate the image
        rotated = ndimage.rotate(image_to_rotate,-90,mode='constant')

        # create full output path, 'example.jpg' 
        # becomes 'rotate_example.jpg', save the file to disk
        fullpath = os.path.join(outPath, ''+image_path)
        imageio.imwrite(fullpath, rotated)

if __name__ == '__main__':
    main()