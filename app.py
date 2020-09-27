import cv2
import numpy as np

frame_width = 840
frame_height = 480

capture = cv2.VideoCapture(0)
# Set width, height and brightness of the capture
capture.set(3, frame_width)
capture.set(4, frame_height)
capture.set(10, 150)

# sets of the colors to detect - hMin, hMax, sMin, sMax, vMin, vMax
color_sets = [[165, 179, 126, 237, 64, 255]]


def find_color(cap):
    # convert image HSV color
    capture_hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    # lower = np.array([h_min, s_min, v_min])
    # upper = np.array([h_max, s_max, v_max])
    # mask = cv2.inRange(capture_hsv, lower, upper)
    # cv2.imshow("Capture", mask)


while True:
    # Capture the frame-by-frame
    ret, frame = capture.read()

    # Display the frames
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

# When everything is done, release the capture
capture.release()
cv2.destroyAllWindows()
