import cv2 as cv

cats = cv.imread("./assets/cats.jpg")
cv.imshow("cats", cats)

cv.waitKey(0)
