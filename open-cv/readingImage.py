import cv2 as cv

# reading image
img = cv.imread("./assets/Flowchart.jpg")
cv.imshow("Tree", img)
cv.waitKey(0)
