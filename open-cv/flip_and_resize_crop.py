import cv2 as cv

img = cv.imread("./assets/small.jpg")
# cv.imshow("image", img)


# resizing an image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow("resized image", resized)


# flipping 1-- x-flip, 0-- y-flip, -(1)-- both
flippedImage = cv.flip(resized, 0)
cv.imshow("flipped image", flippedImage)


# cropping
croppedImage = resized[100:350, 100:450]
cv.imshow("cropped image", croppedImage)


cv.waitKey(0)
