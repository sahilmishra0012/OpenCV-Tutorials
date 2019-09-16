import cv2


#Provide filename to read images or 0 to access camera
cap=cv2.VideoCapture(1)

while(True):
    ret,frame=cap.read()

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# Currently camera drivers are missing on my system.
# So, output file will be added only after installing drivers.