# Program to read, write and show images

import cv2

img=cv2.imread('robin.jpg',1)

#cv2.line(img,(Start Point Tuple),(End Point Tuple),(RGB Tuple),thickness)
img=cv2.line(img,(100,100),(400,500),(255,0,0),5)
img=cv2.arrowedLine(img,(200,100),(600,500),(255,0,0),5)
img=cv2.rectangle(img,(300,300),(900,700),(0,0,0),5)
img=cv2.rectangle(img,(100,100),(200,200),(0,0,0),-1)# -1 fills the shape
img=cv2.circle(img,(450,30),40,(0,255,0),2)# 40 is radius



cv2.imshow('Image Window',img)
k=cv2.waitKey(0)

if k==ord('q'):#  27 is for escape character
    cv2.destroyAllWindows()# To destroy all the windows
# Write Image when s is pressed.
elif k==ord('s'):
    cv2.imwrite('bird.jpg',img)
    cv2.destroyAllWindows()# To destroy all the windows
