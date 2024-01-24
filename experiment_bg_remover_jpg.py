import cv2
import numpy as np

# Read image
img = cv2.imread('gloves.jpg')
hh, ww = img.shape[:2]

# threshold on white
# Define lower and uppper limits
lower = np.array([250, 250, 250])
upper = np.array([255, 255, 255])

# Create mask to only select black
thresh = cv2.inRange(img, lower, upper)

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50, 50))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# invert morph image
mask = cv2.bitwise_not(morph)

# apply mask to image
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.imshow('morph', morph)
cv2.waitKey(0)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save results
cv2.imwrite('pills_thresh.jpg', thresh)
cv2.imwrite('pills_morph.jpg', morph)
cv2.imwrite('pills_mask.jpg', mask)
cv2.imwrite('pills_result.jpg', result)
