import numpy as np 
import cv2 as cv 

textImage=np.zeros((600,700),dtype="uint8")
cv.putText(textImage,"Hello World in OpenCV",(textImage.shape[0]//5,textImage.shape[0]//2),
           cv.FONT_HERSHEY_TRIPLEX,1.0,(233,222,222),2)

cv.imshow("blank",textImage)
cv.waitKey(0)
