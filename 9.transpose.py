import cv2
import numpy as np
img=cv2.imread('robin.jpg',1)
transposed_img=cv2.transpose(img)
cv2.imshow('Image Window',transposed_img)

k=cv2.waitKey(100000)
