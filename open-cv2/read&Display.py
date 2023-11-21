import cv2 as cv
img = cv.imread("./images/cats.jpg")
grayscale_img = cv.imread("./images/cats.jpg", cv.IMREAD_GRAYSCALE)
cv.imshow("boy image", img)

# converting color space
gray_img = cv.cvtColor(img, cv.COLOR_RGB2YUV)
cv.imshow("gray space", gray_img)

# changing image format
# cv.imwrite("./images/output.png", img, [cv.IMWRITE_PNG_COMPRESSION, 5])


# waitkey (argument in milli-seconds to wait for the program)
# if 0 then wait for keyboard key
cv.waitKey(0)
