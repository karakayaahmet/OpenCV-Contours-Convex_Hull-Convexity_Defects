import cv2

# image moments: geometri merkezi (centroid)

img = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

m = cv2.moments(thresh)  # moments

x = int(m["m10"]/m["m00"])
y = int(m["m01"]/m["m00"])

cv2.circle(img, (x,y), 6, (0,0,255), -1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


