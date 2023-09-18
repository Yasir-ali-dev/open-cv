import cv2 as cv

img = cv.imread("./assets/small.jpg")
cv.imshow("image", img)

# increaseing kernel size increases blur (3,3) always pass the odd values to the kernel
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT,)
cv.imshow("blured image", blur)

cv.waitKey(0)
