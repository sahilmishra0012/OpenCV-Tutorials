import cv2
import numpy as np
img=cv2.imread('bird.jpg',1)
height,width=img.shape[:2]
start_row,start_col=int(height*0.2),int(width*0.2)
end_row,end_col=int(height*0.6),int(width*0.6)
img=img[start_row:end_row,start_col:end_col]

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


edges=cv2.Canny(gray,30,200)
contours,heirarchy=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(0,255,0),3)
cv2.imshow('Image Window',img)
k=cv2.waitKey(100000)
print(len(contours))
