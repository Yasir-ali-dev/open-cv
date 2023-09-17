import cv2 as cv
import numpy as np

# (700, 500, 3 ) == (height,weidth,no of color channel)
blank = np.zeros((700, 500, 3), dtype="uint8")  # image datatype "uint8"
# 3 color channels = rgb
blank[:] = 0, 0, 0
cv.imshow("blank", blank)


# 1. paint an image a certain colour
red = blank[:]
red[0:300, 00:300] = 120, 3, 23  # 0,300 height , 0,300 width -->red
# cv.imshow("red", red)


# 2. drawing rectangle
cv.rectangle(blank, (0, 0), (400, 700), (43, 234, 123), thickness=cv.FILLED)
# pass (frame, initial point, target point, color, border thickness -1, cv.FILLED { filled the whole box} )
cv.imshow("blank", blank)


cv.waitKey(0)
