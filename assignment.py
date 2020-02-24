import cv2
import numpy as np
import requests

print(cv2.CAP_PROP_FRAME_WIDTH)
print(cv2.CAP_PROP_FRAME_HEIGHT)

while(True):
    img_res = requests.get("http://192.168.43.1:8080/shot.jpg") # Fetching requests from the IP
    img_arr = np.array(bytearray(img_res.content), dtype = np.uint8) # Converting received contents to matrix

    
    cap=cv2.imdecode(img_arr,-1) # Converting matrix to frame

    # Resizing Frame
    scale_percent = 60 
    width = int(cap.shape[1] * scale_percent / 100)
    height = int(cap.shape[0] * scale_percent / 100)
    dim = (width, height) 
    cap=cv2.resize(cap,dim,interpolation=cv2.INTER_AREA)

    # Displaying Frame
    cv2.imshow('frame', cap)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cv2.destroyAllWindows()
