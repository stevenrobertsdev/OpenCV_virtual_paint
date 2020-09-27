import cv2
import numpy as np

frame_width = 640
frame_height = 480

capture = cv2.VideoCapture(0)
# Set width, height and brightness of the capture
capture.set(3, frame_width)
capture.set(4, frame_height)
capture.set(10, 150)

# sets of the colors to detect - hMin, sMin, vMin, hMax, sMax, vMax
color_sets = [[165, 151, 0, 179, 255, 255],
              [97, 192, 51, 119, 255, 255],
              [82, 125, 18, 112, 255, 97]]

# color values written in BGR not RGB
color_values = [[0, 0, 255],
                [255, 0, 0],
                [0, 255, 0]]

color_names = ['RED', 'BLUE', 'GREEN']


def find_color(cap, colors, values, names):
    capture_hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    count = 0
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(capture_hsv, lower, upper)
        x, y, show_text = get_contours(mask)
        cv2.circle(capture_result, (x, y), 10, values[count], cv2.FILLED)

        if show_text:
            cv2.putText(capture_result, names[count], (320, 400), cv2.FONT_HERSHEY_COMPLEX, 2, values[count], 2)

        count += 1
        # cv2.imshow(str(color[0]), mask)


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h, show_text = 0, 0, 0, 0, False
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            show_text = True
    return x + w // 2, y, show_text


while True:
    # Capture the frame-by-frame
    ret, frame = capture.read()
    # Create copy of frames
    capture_result = frame.copy()
    # apply find color and contours
    find_color(frame, color_sets, color_values, color_names)
    # display frames
    cv2.imshow('Result', capture_result)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

# When everything is done, release the capture
capture.release()
cv2.destroyAllWindows()
