import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)  # frame shape[1] represents width
    height = int(frame.shape[0]*scale)  # frame shape[0] represents height
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("./assets/01.mp4")

while True:
    isTrue, frame = capture.read()
    rescaleImage = rescaleFrame(frame, scale=.3)
    cv.imshow("video", rescaleImage)
    if cv.waitKey(20) & 0xFF == ord("d"):
        break
capture.release()
cv.destroyAllWindows()
