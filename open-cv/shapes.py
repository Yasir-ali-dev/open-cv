import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3),dtype="uint8")
blank[:]=255,255,255
#blank[0:200,250:500]=255,255,255
# cv.imshow("blank", blank)

# rectangle
cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[0]//2),(3,24,233),thickness=-1)
# cv.imshow("rectangle",blank)

#circle
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),50,(233,232,1),thickness=-1)
#cv.imshow("circle with in a rectangle",blank)

# line
cv.line(blank,(100,150),(500,400),(143,123,22),thickness=3)
cv.imshow("blank with a rectangle in circle and line",blank)

cv.waitKey(0)


