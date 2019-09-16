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
cv2.waitKey(0)
cv2.destroyAllWindows()# To destroy all the windows


# Write Image
cv2.imwrite('bird.jpg',img)