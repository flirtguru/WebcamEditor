#IMAGE SEGMENTATION

import cv2
import numpy as np


def sketch(image):
  
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    edges=cv2.Canny(gray,30,200)
    
    lol,contours,hei=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(image,contours,-1,(13,56,100),2)
    
    return image


   
 
cap=cv2.VideoCapture(0)

while True:
    
    ret,frame=cap.read()
    
    cv2.imshow("Editing",sketch(frame))
    
    if cv2.waitKey(1)==13:
        
        break
       
cap.release() 

cv2.destroyAllWindows()    