# Video capture using camera of android phone.
# Using android app IP Webcam to connect webcam to localhost.
import cv2
import numpy as np
import requests

print(cv2.CAP_PROP_FRAME_WIDTH)
print(cv2.CAP_PROP_FRAME_HEIGHT)


while(True):
#Provide filename to read images or 0 to access camera
    img_res = requests.get("http://192.168.43.79:8080/shot.jpg")# Private IP
    img_arr = np.array(bytearray(img_res.content), dtype = np.uint8)

    
    cap=cv2.imdecode(img_arr,-1)
    gray=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cv2.destroyAllWindows()
