# Program to read, write and show images

import cv2

# Read Images
# imread(filename,flag)  flag=1=>Color Image flag=0=>Grayscale flag=-1=>Original Image
img=cv2.imread('robin.jpg',1)
print(img.shape)