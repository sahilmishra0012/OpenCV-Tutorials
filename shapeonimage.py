# Program to read, write and show images

import cv2

img=cv2.imread('robin.jpg',1)

#cv2.line(img,(Start Point Tuple),(End Point Tuple),(RGB Tuple),thickness)
img=cv2.line(img,(100,100),(400,500),(255,0,0),5)

cv2.imshow('Image Window',img)
k=cv2.waitKey(0)

if k==ord('q'):#  27 is for escape character
    cv2.destroyAllWindows()# To destroy all the windows
# Write Image when s is pressed.
elif k==ord('s'):
    cv2.imwrite('bird.jpg',img)
    cv2.destroyAllWindows()# To destroy all the windows
