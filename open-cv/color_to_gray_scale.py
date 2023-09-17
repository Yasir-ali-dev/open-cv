import cv2 as cv

bgr = cv.imread("./assets/small.jpg")
cv.imshow("image", bgr)

# cv.COLOR_BGR2GRAY changes color to grey
gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

cv.waitKey(0)
