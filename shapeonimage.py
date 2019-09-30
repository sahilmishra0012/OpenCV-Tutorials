# Program to read, write and show images

import cv2

img=cv2.imread('robin.jpg',1)

#cv2.line(img,(Start Point Tuple),(End Point Tuple),(RGB Tuple),thickness)
img=cv2.line(img,pt1=(100,100),pt2=(400,500),color=(255,0,0),thickness=5)
img=cv2.arrowedLine(img,pt1=(200,100),pt2=(600,500),color=(255,0,0),thickness=5)
img=cv2.rectangle(img,pt1=(300,300),pt2=(900,700),color=(0,0,0),thickness=5)
img=cv2.rectangle(img,pt1=(100,100),pt2=(200,200),color=(0,0,0),thickness=-1)# -1 fills the shape
img=cv2.circle(img,center=(450,400),radius=40,color=(0,255,0),thickness=2)# 40 is radius

font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,"OpenCV",(200,200),fontFace=font,fontScale=10,color=(0,255,0))


cv2.imshow('Image Window',img)
k=cv2.waitKey(0)

if k==ord('q'):#  27 is for escape character
    cv2.destroyAllWindows()# To destroy all the windows
# Write Image when s is pressed.
elif k==ord('s'):
    cv2.imwrite('bird.jpg',img)
    cv2.destroyAllWindows()# To destroy all the windows
