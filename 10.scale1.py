import cv2
img=cv2.imread('robin.jpg',1)
scaled_img=cv2.resize(img,None,fx=0.5,fy=0.5)
cv2.imshow('Image Window',scaled_img)

k=cv2.waitKey(100000)
