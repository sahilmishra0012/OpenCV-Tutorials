import numpy as np
import cv2



def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(x)+" "+str(y)
        cv2.putText(img,strXY,(x,y),font,0.25,(255,255,0),1)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        red=img[y,x,0]
        green=img[y,x,1]
        blue=img[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY=str(red)+" "+str(green)+" "+str(blue)
        cv2.putText(img,strXY,(x,y),font,0.25,(255,255,0),1)
        cv2.imshow('image',img) 

img=cv2.imread('bird.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
