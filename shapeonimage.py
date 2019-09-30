# Program to read, write and show images

import cv2

img=cv2.imread('robin.jpg',1)
print(img.shape)
cv2.imshow('Image Window',img)
k=cv2.waitKey(0)

if k==27:#  27 is for escape character
    cv2.destroyAllWindows()# To destroy all the windows
# Write Image when s is pressed.
elif k==ord('s'):
    cv2.imwrite('bird.jpg',img)
    cv2.destroyAllWindows()# To destroy all the windows
