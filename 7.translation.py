import cv2
import numpy as np
img=cv2.imread('robin.jpg',1)
height,width=img.shape[:2]
quarter_h,quarter_w=height/4,width/4
T=np.float32([[1,0,quarter_w],[0,1,quarter_h]])
translated_img=cv2.warpAffine(img,T,(height,width))
cv2.imshow('Image Window',translated_img)

k=cv2.waitKey(10000)
