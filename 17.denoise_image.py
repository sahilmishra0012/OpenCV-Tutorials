import cv2
import numpy as np
img=cv2.imread('robin.jpg',1)
height,width=img.shape[:2]
start_row,start_col=int(height*0.2),int(width*0.2)
end_row,end_col=int(height*0.6),int(width*0.6)
img=img[start_row:end_row,start_col:end_col]

sub=cv2.fastNlMeansDenoisingColored(img,None,6,6,7,21)

cv2.imshow('Image Window',sub)
k=cv2.waitKey(100000)
