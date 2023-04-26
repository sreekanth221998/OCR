import cv2
import glob
import os
from scipy import ndimage, misc
import numpy as np
import os
import cv2
import imageio

def main():
    outPath = r"C:\Users\Sreekanth\Desktop\OCR-Thermodata\CROPPED IMAGES"
    path = r"C:\Users\Sreekanth\Desktop\OCR-Thermodata\rotatedimages1"

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        image_to_crop = imageio.imread(input_path)

        # rotate the image
        imgCropped = image_to_crop[0:1500, 0:1500]   #0:1100

        # create full output path, 'example.jpg' 
        # becomes 'rotate_example.jpg', save the file to disk
        fullpath = os.path.join(outPath, ''+image_path)
        imageio.imwrite(fullpath, imgCropped)

if __name__ == '__main__':
    main()
