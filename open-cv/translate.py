import cv2 as cv
import numpy as np


img = cv.imread("./assets/download.jfif")
cv.imshow("img", img)


def translate(img, x, y):
    transMatrix = np.float32([[1, 0, x], [0, 1, y]])
    print(transMatrix)
    # 1- represents width and 0 represents height of image
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)

# -x -- left
# +x -- right
# -y --up
# +y --down


translated = translate(img, -100, -100)
cv.imshow("translated image", translated)


cv.waitKey(0)
