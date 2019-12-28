import cv2
img=cv2.imread('robin.jpg',1)
height,width=img.shape[:2]
start_row,start_col=int(height*0.2),int(width*0.2)
end_row,end_col=int(height*0.6),int(width*0.6)
cropped_img=img[start_row:end_row,start_col:end_col]
cv2.imshow('Image Window',cropped_img)
k=cv2.waitKey(100000)
