# Python program to extract text from all the images in a folder
# storing the text in corresponding files in a different folder
import pytesseract 
import os
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def main():
 # path for the folder for getting the raw images
 path = r"C:\Users\Sreekanth\Desktop\OCR-Thermodata\CROPPED IMAGES"

 # path for the folder for getting the output
 tempPath =r"C:\Users\Sreekanth\Desktop\OCR-Thermodata\LLESUPPLEMENTTEXTFILES"

 # iterating the images inside the folder
 for imageName in os.listdir(path):
   
  inputPath = os.path.join(path, imageName)
  #img = Image.open(inputPath)
  image = cv2.imread(inputPath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
  # Remove horizontal lines
  horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (70,1))
  detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
  cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]
  for c in cnts:
      cv2.drawContours(thresh, [c], -1, (255,255,255), 1)
  vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,60))
  detect_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=1)
  cnts = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]
  for c in cnts:
      cv2.drawContours(thresh, [c], -1, (255,255,255), 2)
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60,1))
  dilate = cv2.dilate(thresh, kernel, iterations=2)
  cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]
  for c in cnts:
      area = cv2.contourArea(c)
      if area < 500:
          cv2.drawContours(dilate, [c], -1, (255,255,255), 1)
  result = cv2.bitwise_or(image, image, mask=dilate)
  result[dilate==0] = (255,255,255) 

  # applying ocr using pytesseract for python
  text = pytesseract.image_to_string(image, lang='eng',config='--psm 6 --oem 3 load_system_dawg=false load_freq_dawg=false')

  # for removing the .jpg from the imagePath
  #imagePath = imagePath[0:-4]
  #fullTempPath = os.path.join(tempPath, imageName+".txt")
  fullTempPath = os.path.join(tempPath,imageName+".txt" ) #''+image_path
  print(text)

  # saving the text for every image in a separate .txt file
  file1 = open(fullTempPath, "w")
  file1.write(text)
  file1.close()

if __name__ == '__main__':
 main()

