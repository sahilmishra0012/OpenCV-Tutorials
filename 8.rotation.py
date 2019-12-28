import cv2
import numpy as np
img=cv2.imread('robin.jpg',1)
height,width=img.shape[:2]
quarter_h,quarter_w=height/4,width/4
r_mat=cv2.getRotationMatrix2D((width/2,height/2),90,1)
translated_img=cv2.warpAffine(img,r_mat,(height,width))
cv2.imshow('Image Window',translated_img)

k=cv2.waitKey(100000)
