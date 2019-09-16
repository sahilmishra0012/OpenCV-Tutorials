# Program to read, write and show images

import cv2

# Read Images
# img=cv2.imread(filename,flag)  flag=1=>Color Image flag=0=>Grayscale flag=-1=>Original Image
img=cv2.imread('robin.jpg',1)
print(img.shape)


# Show Image
# cv2.imshow('Window Name',img)
cv2.imshow('Image Window',img)

#It prevents the window from closing immediately be giving it delay. Put 0 to close it by user
# If delay is 0, then we need to put conditions for closing window else the window 
# remains opened.
k=cv2.waitKey(0)

if k==27:#  27 is for escape character
    cv2.destroyAllWindows()# To destroy all the windows
# Write Image when s is pressed.
elif k==ord('s'):
    cv2.imwrite('bird.jpg',img)