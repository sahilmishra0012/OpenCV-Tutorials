import cv2
img=cv2.imread('robin.jpg',1)
scaled_img=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image Window',scaled_img)

k=cv2.waitKey(100000)
