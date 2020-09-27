import cv2
import numpy as np

frame_width = 840
frame_height = 480

capture = cv2.VideoCapture(0)
# Set width, height and brightness of the capture
capture.set(3, frame_width)
capture.set(4, frame_height)
capture.set(10, 150)


def empty(a):
    pass


cv2.namedWindow('HSV')
cv2.resizeWindow('HSV', 640, 240)

cv2. createTrackbar('Hue Min', 'HSV', 0, 179, empty)
cv2. createTrackbar('Hue Max', 'HSV', 179, 179, empty)
cv2. createTrackbar('Sat Min', 'HSV', 0, 255, empty)
cv2. createTrackbar('Sat Max', 'HSV', 255, 255, empty)
cv2. createTrackbar('Val Min', 'HSV', 0, 255, empty)
cv2. createTrackbar('Val Max', 'HSV', 255, 255, empty)


while True:
    _, frame = capture.read()
    capture_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('Hue Min', 'HSV')
    h_max = cv2.getTrackbarPos('Hue Max', 'HSV')
    s_min = cv2.getTrackbarPos('Sat Min', 'HSV')
    s_max = cv2.getTrackbarPos('Sat Max', 'HSV')
    v_min = cv2.getTrackbarPos('Val Min', 'HSV')
    v_max = cv2.getTrackbarPos('Val Max', 'HSV')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(capture_hsv, lower, upper)

    masked_result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Mask', mask)
    cv2.imshow('Masked result', masked_result)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
