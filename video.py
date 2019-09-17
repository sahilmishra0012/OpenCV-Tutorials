# Video capture using camera of android phone.
# Using android app IP Webcam to connect webcam to localhost.
import cv2
import numpy as np
import requests

while(True):
#Provide filename to read images or 0 to access camera
    img_res = requests.get("http://192.168.43.18:8080/shot.jpg")# Private IP
    img_arr = np.array(bytearray(img_res.content), dtype = np.uint8)
    cap=cv2.imdecode(img_arr,-1)

    cv2.imshow('frame', cap)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
