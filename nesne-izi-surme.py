import cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sensivity = 15
    lower_white = np.array([0,0,255-sensivity]) # hsv code for white
    upper_white = np.array([255,sensivity,255])

    mask = cv2.inRange(hsv,lower_white,upper_white)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()