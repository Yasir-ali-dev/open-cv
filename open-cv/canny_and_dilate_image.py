import cv2 as cv

img = cv.imread("./assets/small.jpg")
# cv.imshow("image", img)

# increaseing kernel size increases blur (3,3)
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)

# edge cascade
# threshhold values -- passing blur img reduces edge cascade
canny = cv.Canny(blur, 300, 270)
cv.imshow("blured image", canny)

# dilate the edges -- means bolding the edges
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("blured image", dilated)

cv.waitKey(0)
