import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    belt = frame[150:330, 180:500]
    gray_capture = cv2.cvtColor(belt, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_capture, 80, 255, cv2.THRESH_BINARY)

    #detect bolts
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        #calculate area
        area = cv2.contourArea(cnt)

        cv2.rectangle(belt, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(belt, str(area), (x, y), 1, 1, (255, 0, 0))

        if 1900 < area < 2200:
            cv2.rectangle(belt, (x, y), (x + w, y + h), (0, 255, 0), 2)
        elif area != 0:
            cv2.rectangle(belt, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # else:
        #     cv2.rectangle(belt, (x, y), (x + w, y + h), (0, 0, 0), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Threshold", threshold)
    key = cv2.waitKey(1)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()

