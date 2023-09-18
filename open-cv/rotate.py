import cv2 as cv

img = cv.imread("./assets/small.jpg")
cv.imshow("image", img)


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    print(img.shape[:2])
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


# rotated = rotate(img, -45)
# cv.imshow("rotated", rotated)
rotated90 = rotate(img, 90)
cv.imshow("rotated 90deg", rotated90)


cv.waitKey(0)
