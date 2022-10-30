import numpy as np
import cv2

img = cv2.imread("star.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray, 127, 255,0)

contours,_ = cv2.findContours(thresh,2,1)

hull = cv2.convexHull(contours[0], returnPoints=False)

defects = cv2.convexityDefects(contours[0], hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(contours[0][s][0])
    end = tuple(contours[0][e][0])
    far = tuple(contours[0][f][0])

    cv2.line(img, start, end, [0,255,0], 2)
    cv2.circle(img, far, 5, [0,255,0], -1)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()