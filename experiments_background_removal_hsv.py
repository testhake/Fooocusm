import cv2
import numpy as np

img = cv2.imread('man.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([0, 0, 120])
upper_blue = np.array([180, 38, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(img, img, mask=mask)
b, g, r = cv2.split(result)
filter = g.copy()

ret, mask = cv2.threshold(filter, 10, 255, 1)

img[mask == 0] = 255

cv2.imwrite('man_result_hsv.jpg', img)
